from fastapi import FastAPI, File, UploadFile
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

app = FastAPI()

connection_string="DefaultEndpointsProtocol=https;AccountName=bhavs222;AccountKey=84xjNyL14WnGOGEUSq+unqL1diZIIi1Uru/I5kROwOtT+KX8hXsOjBoT71eT5lQDvAF39g/zCpQ6+AStRgCdHw==;EndpointSuffix=core.windows.net"

container_name="input"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

@app.post("/uploadfile/")
def create_upload_file(uploadedFile: UploadFile):
    # Upload the created file
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=uploadedFile.filename)
    blob_client.upload_blob(uploadedFile.file.read())
    return {"filename": uploadedFile.filename}