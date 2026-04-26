# AWS Automation using Python (boto3)

Automated AWS resource provisioning using Python (boto3). This project creates an S3 static website and launches an EC2 instance with proper error handling and configuration.

---

## Project Overview

This project demonstrates how to automate AWS infrastructure without manual console interaction.

It includes:

* ✅ S3 bucket creation
* ✅ File upload with correct content-type
* ✅ Static website hosting setup
* ✅ Public access configuration
* ✅ EC2 instance provisioning
* ✅ Error handling for existing resources

---

## Technologies Used

* Python
* boto3 (AWS SDK for Python)
* AWS Services:

  * S3
  * EC2
  * IAM

---

## How to Run

```bash
pip install boto3
python main.py
```

---

## Output

After execution:

* S3 bucket is created (or reused)
* HTML file is uploaded
* Static website is enabled
* EC2 instance is launched

---

## Project Screenshots

### 1. Script Execution Output

`main.py` executed successfully and created AWS resources:

<img width="1920" height="1020" alt="Run Output" src="https://github.com/user-attachments/assets/26a1903c-68ae-4a1e-bb55-f6e193c2e7fc" />

---

### 2. S3 Bucket Created

S3 bucket successfully created and visible in AWS Console:

<img width="1920" height="1020" alt="S3 Bucket" src="https://github.com/user-attachments/assets/4bb70c24-d69c-4591-ae39-4d95556ff1c1" />

---

### 3. S3 Static Website (Live Output)

HTML file uploaded and hosted successfully. Website is live:

<img width="1920" height="1020" alt="S3 Website Output" src="https://github.com/user-attachments/assets/d692da2f-89a8-4533-af1f-206eeb292153" />

---

### 4. EC2 Instance Running

EC2 instance launched successfully and running:

<img width="1920" height="1020" alt="EC2 Instance" src="https://github.com/user-attachments/assets/36de3bc6-ab3d-4342-a1a0-63c624ef71ef" />

---

## Important Notes

* Configure AWS credentials before running:

  ```
  aws configure
  ```
* Do not upload `.pem` key files to GitHub
* Bucket names must be globally unique
* Ensure public access is enabled for S3 static website

---

## Key Learnings

* Automated AWS resource provisioning using boto3
* Handled real-world AWS errors (bucket exists, permissions, etc.)
* Configured S3 for static website hosting
* Launched and managed EC2 instances programmatically

---

## Conclusion

This project demonstrates practical cloud automation skills and real-world AWS usage using Python.

---
