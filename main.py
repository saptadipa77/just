from appwrite.client import Client
from dotenv import load_dotenv
import os
load_dotenv

project_id=os.getenv('APPWRITE_PROJECT_ID')
api_key=os.getenv('APPWRITE_API_KEY')
db_id=os.getenv('APPWRITE_DB_ID')
db_collection_id=os.getenv('APPWRITE_COLLECTION_ID')

client=Client()
client=(client
        .set_endpoint('https://cloud.appwrite.io/v1') # your api endpoint
        .set_project(project_id) #your project ID
        .set_key(api_key) # your secret API key
        )
