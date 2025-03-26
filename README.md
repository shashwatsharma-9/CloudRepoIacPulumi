# AWS S3 Static Website Deployment using Pulumi

## Overview  
This project automates the deployment of a **static website** on **AWS S3** using **Pulumi**. It provisions an S3 bucket, uploads site files dynamically, and sets up public access policies for hosting.  

## Features  
- Creates an S3 bucket with **static website hosting enabled**  
- Uploads files dynamically from a local directory  
- Configures a **public bucket policy** for seamless access  
- Automates the entire infrastructure setup using **Pulumi**  

## Prerequisites  
- **AWS CLI** installed and configured  
- **Pulumi CLI** installed  
- **Python** (for Pulumi scripting)  
- **Git** for version control  

## Installation and Usage  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/shashwatsharma-9/CloudRepoIacPulumi.git
cd CloudRepoIacPulumi
```

### 2️⃣ Install Dependencies
```sh
pip install pulumi pulumi-aws
```

### 3️⃣ Set Up Pulumi
#### Login to Pulumi
```sh
pulumi login
```
#### Initialize a New Stack
```sh
pulumi stack init dev
```
#### Set AWS Region
```sh
pulumi config set aws:region us-east-1
```
#### Set Local Directory for Site Files
```sh
pulumi config set siteDir ./site
```

### 4️⃣ Deploy to AWS
```sh
pulumi up
```

### 5️⃣ Get Website URL
```sh
pulumi stack output bucket_website_url
```

## 🔥 Cleanup
To destroy the infrastructure:
```sh
pulumi destroy
```
⚠️ **This action will delete all deployed resources.**

## 📂 Repository Structure
```
📂 CloudRepoIacPulumi  
 ├── 📂 site (Static website files)  
 ├── 📄 __main__.py (Pulumi script)  
 ├── 📄 Pulumi.yaml  
 ├── 📄 Pulumi.dev.yaml  
 ├── 📄 README.md  
