#USER/PICTURE_HANDLER.PY

import os
from PIL import Image
from flask import current_app

def add_profile_pic(pic_upload, username):
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]  # Get file extension
    storage_filename = f"{username}.{ext_type}"

    # Use os.path.join correctly with forward slashes or raw strings
    filepath = os.path.join(current_app.root_path, 'static', 'profile_pics', storage_filename)

    # Resize image
    output_size = (200, 200)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
