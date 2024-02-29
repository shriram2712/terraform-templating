from jinja2 import Environment, FileSystemLoader
import os
import shutil
import json
from distutils.dir_util import copy_tree
import yaml

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