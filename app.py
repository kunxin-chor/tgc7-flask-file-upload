from flask import Flask, render_template, request, redirect, url_for
import os
import gallery

# allow us to read in the variables from our .env files
from dotenv import load_dotenv
load_dotenv()

CLOUD_NAME = os.environ.get('CLOUD_NAME')
UPLOAD_PRESET = os.environ.get('UPLOAD_PRESET')

app = Flask(__name__)

gallery.load()


@app.route('/')
def display_gallery():
    images = gallery.get_database()
    return render_template('gallery.template.html', images=images)


@app.route('/upload-image')
def display_upload_route():
    return render_template('upload_image.template.html', cloud_name=CLOUD_NAME,
                           upload_preset=UPLOAD_PRESET)


@app.route('/edit-image/<image_id>')
def edit_image(image_id):
    image = gallery.get_image(image_id)
    return render_template('edit_image.template.html', cloud_name=CLOUD_NAME,
                           upload_preset=UPLOAD_PRESET, image=image)


@app.route('/edit-image/<image_id>', methods=["POST"])
def process_edit_image(image_id):
    caption = request.form.get('caption')
    url = request.form.get('uploaded-file-url')
    asset_id = request.form.get('asset-id')
    gallery.update(image_id, asset_id, url, caption)
    return "image upated"


@app.route('/upload-image', methods=["POST"])
def process_upload():
    caption = request.form.get('caption')
    url = request.form.get('uploaded-file-url')
    asset_id = request.form.get('asset-id')
    gallery.put(asset_id, url, caption)
    gallery.save()
    return "image added"


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
