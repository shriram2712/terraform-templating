from jinja2 import Environment, FileSystemLoader
import os
import shutil
import json

environment = Environment(loader=FileSystemLoader("templates/"))

accounts = [
    {
        "account_id" : "test_account",
        "regions" :  [ {
            "enable_vpc" : "true",
            "region"     : "us-east-1",
            "vpc"        : {
                "name"  : "test-vpc"
            },
            "subnets"  : [
                {
                    "name": "subnetone",
                    "cidr_block": "172.20.0.0/24"
                },
                {
                    "name": "subnettwo",
                    "cidr_block": "172.20.1.0/24"
                }
            ],
            "enable_ec2" : "true",
            "ec2list" : [
                {
                    "name" : "ec2one",
                    "subnet_name" : "subnetone"
                },
                {
                    "name" : "ec2two",
                    "subnet_name" : "subnettwo"
                }
            ]
        },
        {
            "enable_vpc" : "true",
            "region"     : "us-east-2",
            "vpc"        : {
                "name"  : "test-vpc"
            },
            "subnets"  : [
                {
                    "name": "subnetone",
                    "cidr_block": "172.20.0.0/24"
                },
                {
                    "name": "subnettwo",
                    "cidr_block": "172.20.1.0/24"
                }
            ],
            "enable_ec2" : "true",
            "ec2list" : [
                {
                    "name" : "ec2one",
                    "subnet_name" : "subnetone"
                },
                {
                    "name" : "ec2two",
                    "subnet_name" : "subnettwo"
                }
            ]
        }   
        ]
    }, 
    
     {
        "account_id" : "test_account2",
        "regions" :  [ {
            "enable_vpc" : "true",
            "region"     : "us-west-1",
            "vpc"        : {
                "name"  : "test-vpc"
            },
            "subnets"  : [
                {
                    "name": "subnetone",
                    "cidr_block": "172.20.0.0/24"
                },
                {
                    "name": "subnettwo",
                    "cidr_block": "172.20.1.0/24"
                }
            ],
            "enable_ec2" : "false",
        },   
        ]
    }, 
    

]

for account in accounts:
    path = "terraform-files/"+account["account_id"]
    if not os.path.exists(path):
        os.mkdir(path)    
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
    