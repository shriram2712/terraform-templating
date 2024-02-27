terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~5.36.0"
    }
  }
}


provider "aws" {
    region = us-east-1
    alias = test_account-us-east-1
}

provider "aws" {
    region = us-east-2
    alias = test_account-us-east-2
}
