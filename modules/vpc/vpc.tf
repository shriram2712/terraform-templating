resource "aws_vpc" "main" {
  cidr_block = "172.20.0.0/16"
  tags = {
    Name = var.name
  }

}