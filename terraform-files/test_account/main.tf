#Generated from Terraform template in Jinja



    
        module "vpc_test_account_us-east-1_test-vpc" {
            source = "../modules/vpc"
            providers = {
                aws = aws.test_account-us-east-1
            }
            name = "test-vpc"
        }

        
            module "subnet_test_account_us-east-1_subnetone" {
                source = "../modules/subnet"
                providers = {
                    aws = aws.test_account-us-east-1
                }
                vpc_id = module.vpc_test_account_us-east-1_test-vpc.id
                name = subnetone
                cidr_block = "172.20.0.0/24"
            }
        
            module "subnet_test_account_us-east-1_subnettwo" {
                source = "../modules/subnet"
                providers = {
                    aws = aws.test_account-us-east-1
                }
                vpc_id = module.vpc_test_account_us-east-1_test-vpc.id
                name = subnettwo
                cidr_block = "172.20.1.0/24"
            }
        
    

    
    
        module "ec2_test_account_us-east-1" {
            for_each = var.ec2list_test_account_us-east-1
            source = "../modules/ec2"
            providers = {
                aws = aws.test_account-us-east-1
            }
            name = each.value.name
            subnet_id = "module.subnet_test_account_us-east-1_${each.value.subnet_name}.id"
        }
    
    

    
        module "vpc_test_account_us-east-2_test-vpc" {
            source = "../modules/vpc"
            providers = {
                aws = aws.test_account-us-east-2
            }
            name = "test-vpc"
        }

        
            module "subnet_test_account_us-east-2_subnetone" {
                source = "../modules/subnet"
                providers = {
                    aws = aws.test_account-us-east-2
                }
                vpc_id = module.vpc_test_account_us-east-2_test-vpc.id
                name = subnetone
                cidr_block = "172.20.0.0/24"
            }
        
            module "subnet_test_account_us-east-2_subnettwo" {
                source = "../modules/subnet"
                providers = {
                    aws = aws.test_account-us-east-2
                }
                vpc_id = module.vpc_test_account_us-east-2_test-vpc.id
                name = subnettwo
                cidr_block = "172.20.1.0/24"
            }
        
    

    
    
        module "ec2_test_account_us-east-2" {
            for_each = var.ec2list_test_account_us-east-2
            source = "../modules/ec2"
            providers = {
                aws = aws.test_account-us-east-2
            }
            name = each.value.name
            subnet_id = "module.subnet_test_account_us-east-2_${each.value.subnet_name}.id"
        }
    
    

