#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Run by typing
#      python3 flask_app.py
# in a terminal (or just ./main.py).

## **IMPORTANT:** only collaborators on the project where you run
## this can access this web server!

# import basics
import os
import cv2
import numpy as np

# import stuff for our web server
from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory
from flask import jsonify
from utils import get_base_url, allowed_file, and_syntax

# import stuff for our models
import torch
from aitextgen import aitextgen
# load up the model into memory
# you will need to have all your trained model into the folder trained_mode.
ai = aitextgen(model_folder="trained_model", to_gpu=False)

# someone can figure out how to quantize a model. 
# it can speed up inference by about 15%
# ai_quantized = torch.quantization.quantize_dynamic(ai, {torch.nn.Linear}, dtype=torch.qint8)

"""
    Bonus points if you want to have internship at AI Camp
    1. How can we save what user built? And if we can save them, like allow them to publish, can we load the saved results back on the home page? 
    2. Can you add a button for each generated item at the frontend to just allow that item to be added to the story that the user is building? 
    3. What other features you'd like to develop to help AI write better with a user? 
"""


# setup the webservver
port = 12345
base_url = get_base_url(port)
app = Flask(__name__, static_url_path=base_url+'static')


#@app.route(base_url)
@app.route('/')
def home():
    return render_template('home copy.html', generated=None)


@app.route('/', methods=['POST'])
def home_post():
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('Write-your-story-with-AI.html', generated=None)


@app.route('/generate_text', methods=["POST"])
def generate_text():
    """view function that will return json response for generated text. 
    """

    prompt = request.form['prompt']
    if prompt is not None:
        generated = ai.generate(
            n=3,
            batch_size=3,
            prompt=str(prompt),
            max_length=50,
            temperature=0.9,
            return_as_list=True
        )

        
    print('ai generated this:\n')
    print(generated)

    data = {'generated_ls': generated}

    return jsonify(data)

if __name__ == "__main__":
    # change the code.ai-camp.org to the site where you are editing this file.
    print("Try to open\n\n    https://coding.ai-camp.org" + base_url + '\n\n')
    # remove debug=True when deploying it
    app.run(host = '0.0.0.0', port=port, debug=True)
    import sys; sys.exit(0)
