from flask import Blueprint, render_template, request
import re
import base64
import numpy as np
 
def parse_image(imgData):
    img_str = re.search(b"base64,(.*)", imgData).group(1)
    img_decode = base64.decodebytes(img_str)
    with open('output.png', "wb") as f:
        f.write(img_decode)
    return img_decode
 
# Load your model here
model = None
 
upload_api = Blueprint('upload_api', __name__)
 
 
@upload_api.route('/upload/', methods=['POST'])
def upload():
    image = parse_image(request.get_data())
    # Your prediction here
    prediction = 0
    return str(prediction)
 