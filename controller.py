#!usr/bin/env python3
import random
from datetime import datetime
# import model as m

from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)

HUMANIZE_USE_UTC = True

@app.route('/',methods=['GET'])
@app.route('/menu',methods=['GET'])
def menu():
    if request.method=="GET":
        return render_template('menu.html')
    else:
        return render_template('menu.html')

@app.route('/display',methods=['GET'])
def display():
    if request.method=="GET":
        return render_template('display.html')
    else:
        return render_template('display.html')


if __name__ == '__main__':
    app.run(debug=True)