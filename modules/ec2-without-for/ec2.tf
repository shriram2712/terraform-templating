data "aws_ami" "ami" {
  most_recent = true
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm*"]
  }

}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ami.id
  instance_type = "t3.micro"
  subnet_id     = var.subnet_id
  tags = {
    Name = var.name
  }
}