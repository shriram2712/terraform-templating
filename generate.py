from jinja2 import Environment, FileSystemLoader
import os
import shutil
import json
from distutils.dir_util import copy_tree
import yaml
import tarfile
import requests

environment = Environment(loader=FileSystemLoader("templates/"))
accounts = []
accounts_yaml = []
with open('accounts-info.json') as json_file:
    accounts = json.load(json_file)
    accounts_yaml = yaml.dump(accounts)

# with open('accounts-info.yaml', mode="w", encoding="utf-8") as code:
#     code.write(accounts_yaml)

for account in accounts:
    path = "terraform-files/"+account["account_id"]
    if not os.path.exists(path):
        os.mkdir(path)    
        os.mkdir(path+"/modules")
    template = environment.get_template("main-tf-foreach-loop-jinja.txt")
    content = template.render(account)
    
    with open(path+"/main.tf", mode="w", encoding="utf-8") as code:
        code.write(content)

    template = environment.get_template("providers-tf-jinja.txt")
    content = template.render(account)

    with open(path+"/providers.tf", mode="w", encoding="utf-8") as code:
        code.write(content)

    template = environment.get_template("variables-tf-jinja.txt")
    content = template.render(account)

    with open(path+"/variables.tf", mode="w", encoding="utf-8") as code:
        code.write(content)

    template = environment.get_template("tf-vars-jinja.txt")
    content = template.render(account)

    with open(path+"/terraform.auto.tfvars", mode="w", encoding="utf-8") as code:
        content = str(content).replace("'",'"')
        code.write(content)


    shutil.copyfile("./templates/outputs-tf-jinja.txt", path+"/outputs.tf")
    
    copy_tree ("./modules", path+"/modules")
    print(path)
    shutil.make_archive(path,format="gztar", root_dir=path)

    API_ENDPOINT = "https://app.terraform.io/api/v2/organizations/{ORG_NAME}/workspaces"
    CONFIG_VERSION_ENDPOINT = "https://app.terraform.io/api/v2/workspaces"
    api_token = os.getenv('TF_API_TOKEN')
    
    headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/vnd.api+json",
    }    

    print(path)
    workspace_name = account["account_id"]

    try:
        response = requests.get(API_ENDPOINT.format(ORG_NAME="shriramrajaraman")+"/"+workspace_name, headers=headers)
        workspace_id = response.json()["data"]["id"]
        print(path)
        print(workspace_id)
        config_version = {"data":{"type":"configuration-versions"}}
        json_config_version = json.dumps(config_version)
        response = requests.post(CONFIG_VERSION_ENDPOINT+"/"+workspace_id+"/configuration-versions", headers=headers, data=json_config_version)
        upload_url = response.json()
        upload_url = response.json()["data"]["attributes"]["upload-url"]

        headers_octet_stream = {
            "Content-Type": "application/octet-stream"
        }

        with open(path+".tar.gz", 'rb') as data:
            data_binary = data.read()

        response = requests.put(upload_url, headers=headers_octet_stream, data=data_binary)

        print("Run Triggered for workspace ", account["account_id"])
    except requests.exceptions.RequestException as e:
        print(e)