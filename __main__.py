"""A Python Pulumi program"""

import pulumi


import pulumi_aws as aws



vpc = aws.ec2.Vpc("My-VPC-Asad1-test",
    cidr_block="10.1.0.0/16",
    enable_dns_hostnames=True,
    enable_dns_support=True
    )

