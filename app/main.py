# Run by typing python3 main.py

## **IMPORTANT:** only collaborators on the project where you run
## this can access this web server!

"""
    Bonus points if you want to have internship at AI Camp
    1. How can we save what user built? And if we can save them, like allow them to publish, can we load the saved results back on the home page? 
    2. Can you add a button for each generated item at the frontend to just allow that item to be added to the story that the user is building? 
    3. What other features you'd like to develop to help AI write better with a user? 
    4. How to speed up the model run? Quantize the model? Using a GPU to run the model? 
"""

# import basics
import os

# import stuff for our web server
from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory
from flask import jsonify
from utils import get_base_url, allowed_file, and_syntax

# import stuff for our models
import torch
# from aitextgen import aitextgen

from models.mime import generate_mime


'''
Coding center code - comment out the following 4 lines of code when ready for production
'''
# load up the model into memory
# you will need to have all your trained model in the app/ directory.
# ai = aitextgen(to_gpu=False)

from transformers import AutoModelWithLMHead, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-small')

model_sb = AutoModelWithLMHead.from_pretrained('models/spongebot')
model_ms = AutoModelWithLMHead.from_pretrained('models/michaelsbot')
model_gr = AutoModelWithLMHead.from_pretrained('models/gordon_rambot')


# model_mine = mine()
# model_groof = groot()




# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
# port = 47474
# base_url = get_base_url(port)
# app = Flask(__name__, static_url_path=base_url+'static')

'''
Deployment code - uncomment the following line of code when ready for production
'''
app = Flask(__name__)

@app.route('/')
# @app.route(base_url)
def home():
    return render_template('Home.html', generated=None)

@app.route('/', methods=['POST'])
# @app.route(base_url, methods=['POST'])
def home_post():
    return redirect(url_for('spongebot'))

### about us page
@app.route('/aboutus')
# @app.route(base_url + '/aboutus')
def aboutus():
    return render_template('About-Us.html', generated=None)



### spongebot page
@app.route('/spongebot')

# @app.route(base_url + '/spongebot')
def spongebot():
    return render_template('sb-cp.html', generated=None)

@app.route('/generate_text_sb', methods=["POST"])
# @app.route(base_url + '/generate_text_sb', methods=["POST"])
def generate_sb():
    user_input = request.args.get('prompt')
    # user_input = request.form['prompt']

    new_user_input_ids = tokenizer.encode(str(user_input) + tokenizer.eos_token, return_tensors='pt')
    # bot_input_ids = torch.cat([new_user_input_ids], dim=-1)

    chat_history_ids = model_sb.generate(
            new_user_input_ids, max_length=400,
            pad_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=2,
            do_sample=True,
            top_k=100,
            top_p=1,
            temperature=0.8)
    
    generated = tokenizer.decode(chat_history_ids[:,new_user_input_ids.shape[-1]:][0], skip_special_tokens=True)
    n = 0
    while n == 0:
        if generated == '':
            chat_history_ids = model_sb.generate(
            bot_input_ids, max_length=100,
            pad_token_id=tokenizer.eos_token_id,  
            no_repeat_ngram_size=2,       
            do_sample=True, 
            top_k=100, 
            top_p=1,
            temperature=0.8)

            generated = tokenizer.decode(chat_history_ids[:,new_user_input_ids.shape[-1]:][0], skip_special_tokens=True)
        else:
            n = 1
            
        
        
    data = {'generated_ls': generated}
    return jsonify(data)





### michael sbot page

@app.route('/michaelsbot')
# @app.route(base_url + '/michaelsbot')
def michaelsbot():
    return render_template('ms-cp.html', generated=None)

@app.route('/generate_text_ms', methods=["POST"])
# @app.route(base_url + '/generate_text_ms', methods=["POST"])
def generate_ms():
    user_input = request.form['prompt']
    print(user_input)
    # user_input = request.args.get('msg')

    new_user_input_ids = tokenizer.encode(str(user_input) + tokenizer.eos_token, return_tensors='pt')
    # bot_input_ids = torch.cat([new_user_input_ids], dim=-1)

    chat_history_ids = model_ms.generate(
            new_user_input_ids, max_length=210,
            pad_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=2,
            do_sample=True,
            top_k=100,
            top_p=0.8,
            temperature=0.8)

    generated = tokenizer.decode(chat_history_ids[:, new_user_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(generated)
    data = {'generated_ls': generated}
    return jsonify(data)






### gordon rambot page

@app.route('/gordonrambot')
# @app.route(base_url + '/gordonrambot')
def gordonrambot():
    return render_template('gr-cp.html', generated=None)

@app.route('/generate_text_gr', methods=["POST"])
# @app.route(base_url + '/generate_text_gr', methods=["POST"])
def generate_gr():
    user_input = request.form['prompt']
    print(user_input)
    # user_input = request.args.get('msg')

    new_user_input_ids = tokenizer.encode(str(user_input) + tokenizer.eos_token, return_tensors='pt')
    # bot_input_ids = torch.cat([new_user_input_ids], dim=-1)

    chat_history_ids = model_gr.generate(
            new_user_input_ids, max_length=210,
            pad_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=2,
            do_sample=True,
            top_k=100,
            top_p=0.8,
            temperature=0.6)

    generated = tokenizer.decode(chat_history_ids[:, new_user_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(generated)
    data = {'generated_ls': generated}
    return jsonify(data)





### groot page
@app.route('/groot')
# @app.route(base_url + '/groot')
def groot():
    return render_template('ms-g.html', generated=None)

@app.route('/generate_text_g', methods=["POST"])
# @app.route(base_url + '/generate_text_g', methods=["POST"])
def generate_groot():
    generated = "I am groot."
    # convert user_input text to array of numbers 
    data = {'generated_ls': generated}
    return jsonify(data)






### mime page
@app.route('/mime')
# @app.route(base_url + '/mime')
def mime():
    return render_template('mime-cp.html', generated=None)

@app.route('/generate_text_m', methods=["POST"])
# @app.route(base_url + '/generate_text_m', methods=["POST"])
def generate_m():
    user_input = request.form['prompt']
    generated = generate_mime(user_input)
    data = {'generated_ls': generated}
    return jsonify(data)











if __name__ == "__main__":
    '''
    coding center code
    '''
    # IMPORTANT: change the cocalcx.ai-camp.org to the site where you are editing this file.
    website_url = 'cocalc5.ai-camp.org'
    print(f"Try to open\n\n    https://{website_url}" + base_url + '\n\n')

    app.run(host = '0.0.0.0', port=port, debug=True)
    import sys; sys.exit(0)

    '''
    scaffold code
    '''
    # Only for debugging while developing
    # app.run(port=80, debug=True)
