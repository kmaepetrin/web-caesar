from flask import Flask, request, redirect, render_template
from caesar import rotate_string
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>
<html>
    <head>
        <title>Caesar Cipher</title>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form method='POST'>
        <label>Rotate by:
            <input type="text" name="rot" value="0"/>
        </label>
        <textarea name="text">
            {0}
        </textarea>
        <button name="Submit query">Submit Query</button>
    </form>
    </body>
</html
"""

@app.route('/', methods=['POST'])
def encrypt():
    text = request.form["text"]
    rot_str = request.form["rot"]
    rot = int(rot_str)

    encrypted = rotate_string(text, rot)

    return form.format(encrypted)

@app.route('/')
def index():
    n = ""

    return form.format(n)

app.run()