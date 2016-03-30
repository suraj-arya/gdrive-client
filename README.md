# gdrive-client

An simpler lightweight version of google drive api client if you only want to list/upload files

## installation

you can install it from github

```bash
pip install git+https://github.com/loanzen/gdrive-client.git
```

now you can use the client,

pass service account email id and private key string to instantiate the client

```python
client = GDriveClient(GDRIVE_CLIENT_EMAIL, GDRIVE_PRIVATE_KEY)
```

now you can use all the available apis from GDriveClient

```python
client.get_or_create_folder(FOLDER_NAME, PARENT_FOLDER_ID)
```

list all the files in a folder with given id

```python
client.list_files_in_folder(FOLDER_ID)
```

to upload a file to gdrive to a particular folder with id PARENT_ID,
If you don't pass PARENT_ID it will upload the file at root.

```python
client.upload_file(FILE_NAME, FILE_PATH_OR_FILE_OBJECT, PARENT_ID, IS_IN_MEMORY_STREAM)
```