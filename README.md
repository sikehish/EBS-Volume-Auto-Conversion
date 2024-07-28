# EBS-Volume-Auto-Conversion
We use AWS cloud watch in combination with AWS Lambda to govern the resources according to the policies. Here, we trigger a Lambda function when an Amazon Elastic Block Store (EBS) volume is created. We use Amazon CloudWatch Events. CloudWatch Events that allows us to monitor and respond to EBS volumes that are of type GP2 and convert them to GP3.
