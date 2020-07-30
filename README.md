# Flask/Cloudinary Demo

## Requirements

From requirements.txt:
```
click==7.1.2
Flask==1.1.2
itsdangerous==1.1.0
python-dotenv==0.14.0
Werkzeug==1.0.1
```

If setting up the project for the first time:

```
pip3 install -r requirements.txt
```

## Add in variables to the .env file

```
export CLOUD_NAME="<your-cloud-name>"
export UPLOAD_PRESET="<your-upload-preset>"
```

To set the upload preset, go the `settings` (the gear at the upper right corner) and
select the `Upload` tab, and scroll down till you can see upload presets.

## Create .gitignore file so that our .env file is not pushed to the github repoistory
Add `.env` to the `.gitignore` file.