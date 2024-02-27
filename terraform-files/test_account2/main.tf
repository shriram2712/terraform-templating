#Generated from Terraform template in Jinja



    
        module "vpc_test_account2_us-west-1_test-vpc" {
            source = "../modules/vpc"
            providers = {
                aws = aws.test_account2-us-west-1
            }
            name = "test-vpc"
        }

        
            module "subnet_test_account2_us-west-1_subnetone" {
                source = "../modules/subnet"
                providers = {
                    aws = aws.test_account2-us-west-1
                }
                vpc_id = module.vpc_test_account2_us-west-1_test-vpc.id
                name = subnetone
                cidr_block = "172.20.0.0/24"
            }
        
            module "subnet_test_account2_us-west-1_subnettwo" {
                source = "../modules/subnet"
                providers = {
                    aws = aws.test_account2-us-west-1
                }
                vpc_id = module.vpc_test_account2_us-west-1_test-vpc.id
                name = subnettwo
                cidr_block = "172.20.1.0/24"
            }
        
    

    
    
    

