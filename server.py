import requests
import urllib.request
import re
import numpy as np
import os, sys, time
import datetime
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from time import sleep
import random
from urllib.request import HTTPError
from urllib.request import URLError
from flask import Flask, render_template, request, jsonify
from threading import Thread
from task_mail import mailfunc

app = Flask(__name__)

@app.route('/')

def index():
    return render_template("mainpage.html")



@app.route("/post",methods=['POST'])
def post():
    code = request.form['subject_code']
    c_num = request.form['c_num']
    mail = request.form['mail']

    thread = Thread(target=mailfunc, args=(code,c_num,mail,))
    thread.daemon = True
    thread.start()
    return render_template("mainpage.html")

if __name__ == '__main__':
    app.run(threaded=True)
