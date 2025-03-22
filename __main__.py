import pulumi
import pulumi_aws as aws
import os
import mimetypes
import json

# Load Pulumi config
config = pulumi.Config()

# Get the site directory from Pulumi configuration
site_dir = config.require("siteDir")

# Create an S3 bucket with website hosting enabled
bucket = aws.s3.Bucket("my-unique-bucket-shashwat",
    website={"index_document": "portfolio.html"},
    force_destroy=True  # Allows deletion of bucket even if it contains files
)

# Store uploaded objects
objects = []

# Upload all files from site_dir to S3 bucket
for file in os.listdir(site_dir):
    filepath = os.path.join(site_dir, file)
    
    # Guess MIME type for proper content delivery
    mime_type, _ = mimetypes.guess_type(filepath)
    mime_type = mime_type if mime_type else "application/octet-stream"

    # Upload each file as an S3 object
    obj = aws.s3.BucketObject(file,  # Use file name as unique key
        bucket=bucket.id,
        source=pulumi.FileAsset(filepath),
        content_type=mime_type
    )
    
    # Store object IDs for export
    objects.append(obj.id)

# Define a public bucket policy
bucket_policy = aws.s3.BucketPolicy("publicAccessPolicy",
    bucket=bucket.id,
    policy=bucket.id.apply(lambda bucket_name: json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{bucket_name}/*"  # Allows public read access
        }]
    }))
)

# Export important outputs
pulumi.export("bucket_name", bucket.id)
pulumi.export("object_keys", objects)  # Export list of all uploaded objects
pulumi.export("bucket_website_url", pulumi.Output.concat("http://", bucket.website_endpoint))
