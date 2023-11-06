# flask_5_tailwind

To set up CDN on GCP:

1. Select Create a Cloud Storage bucket

2. Select Cloud Storage 

3. Select Buckets

4. Select Create

5. Name Bucket

6. Choose where to store data

7. Choose storage class

8. Configure control access to objects

9. Choose how to protect object data 

10. Click create

11. Allow Public access by clearing the check box for Enforce public access prevention 

12. Click Confirm.

13. Upload content to bucket
    
15. click Next.

To Deploy Flask App in GCP:

1. Select App Engine and create
2. Enable APIs
3. Initialize SDK with `gcloud init` in terminal
4. input in terminal `gcloud config set project [project ID]`
5. input in terminal `gcloud app deploy app.yaml`
6. Website url is then provided.
7. 
