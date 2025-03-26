import pulumi
import pulumi_aws as aws
import os
import mimetypes
import json


config = pulumi.Config()


site_dir = config.require("siteDir")


bucket = aws.s3.Bucket("my-unique-bucket-shashwat",
    website={"index_document": "portfolio.html"},
    force_destroy=True  
)


objects = []


for file in os.listdir(site_dir):
    filepath = os.path.join(site_dir, file)
    
    
    mime_type, _ = mimetypes.guess_type(filepath)
    mime_type = mime_type if mime_type else "application/octet-stream"

   
    obj = aws.s3.BucketObject(file,  
        bucket=bucket.id,
        source=pulumi.FileAsset(filepath),
        content_type=mime_type
    )
    
    
    objects.append(obj.id)


bucket_policy = aws.s3.BucketPolicy("publicAccessPolicy",
    bucket=bucket.id,
    policy=bucket.id.apply(lambda bucket_name: json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{bucket_name}/*"
        }]
    }))
)


pulumi.export("bucket_name", bucket.id)
pulumi.export("object_keys", objects)  
pulumi.export("bucket_website_url", pulumi.Output.concat("http://", bucket.website_endpoint))
