data "aws_ami" "ami" {
    most_recent = true
    filter {
        name   = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

}

resource "aws_instance" "web" {
    ami = data.aws_ami.ami.id
    instance_type = "t3.micro"
    subnet_id = var.subnet_id
    tags = {
        Name = var.name
    }
}