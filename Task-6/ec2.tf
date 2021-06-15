provider "aws" {
  region="ap-south-1"
  profile="default"
}

# STEP-1 ( Provisioning OS )

resource "aws_instance" "os1" {
  ami = "ami-010aff33ed5991201"
  security_groups = [ "launch-wizard-46" ]
  instance_type = "t2.small"
  tags = {
	  Name = "terraform instance-1 "
	 }
}

output "my_public_ip_is" {
 value = aws_instance.os1.public_ip

}

output "my_zone_is" {
 value = aws_instance.os1.availability_zone
}

output "my_terraform_instance_id_is" {
 value = aws_instance.os1.id
}

# STEP-2 ( Provisioning EBS volume)

resource "aws_ebs_volume" "storage1" {
  availability_zone = aws_instance.os1.availability_zone
  size              = 10

  tags = {
    Name = "volume-1 for terraform instance-1"
  }
}

output "volume_id_is" {
  value = aws_ebs_volume.storage1.id
}

# STEP-3 ( aws_volume_attachment )

resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdh"
  volume_id   = aws_ebs_volume.storage1.id
  instance_id = aws_instance.os1.id
}

output "attach" {
  value = aws_volume_attachment.ebs_att
}
