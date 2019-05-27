from flask import Flask
app = Flask(__name__)
import cv2

from collections import Counter

import numpy as np
from PIL import Image
from flask import request, render_template



@app.route('/', methods=['GET', 'POST'])
def get_image():
    return render_template('labelTool.html')

if __name__ == '__main__':
	app.run()

