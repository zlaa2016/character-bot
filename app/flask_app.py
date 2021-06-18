# Run by typing main.py

## **IMPORTANT:** only collaborators on the project where you run
## this can access this web server!

"""
    Bonus points if you want to have internship at AI Camp
    1. How can we save what user built? And if we can save them, like allow them to publish, can we load the saved results back on the home page? 
    2. Can you add a button for each generated item at the frontend to just allow that item to be added to the story that the user is building? 
    3. What other features you'd like to develop to help AI write better with a user? 
    4. How to speed up the model run? Quantize the model? Using a GPU to run the model? 
"""

import os

# import stuff for our web server
from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory
from flask import jsonify
from utils import allowed_file, and_syntax

# import stuff for our models
import torch
from aitextgen import aitextgen

# load up the model into memory
# you will need to have all your trained model into the folder trained_mode.
ai = aitextgen(to_gpu=False)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('writer_home.html', generated=None)

@app.route('/', methods=['POST'])
def home_post():
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('Write-your-story-with-AI.html', generated=None)

@app.route('/generate_text', methods=["POST"])
def generate_text():
    """
    view function that will return json response for generated text. 
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

    data = {'generated_ls': generated}

    return jsonify(data)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)
