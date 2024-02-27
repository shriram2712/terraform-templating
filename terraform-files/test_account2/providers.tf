terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~5.36.0"
    }
  }
}


provider "aws" {
    region = us-west-1
    alias = test_account2-us-west-1
}
