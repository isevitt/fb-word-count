from lxml import html
import requests
import re
import urllib.request
from inscriptis import get_text
from flask import Flask, request, url_for, render_template
from collections import Counter

import sys
app = Flask(__name__)

def scrape(url):
    html = urllib.request.urlopen(url).read().decode('utf-8')
    return html

def get_list_words(html):
    text = get_text(html)
    chars_to_replace = ["*", "/", "\\", "?", "!",  "\t", "&", "'", "-", ".", "," "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "$", "©"]
    for i in chars_to_replace:
        text = text.replace(i, "")
    text = text.replace("\n", " ")
    text = re.sub(' +', ' ', text)
    list_of_words = text.split(" ")
    return list_of_words

@app.route('/')
def main_page():
    if request.method == "POST":
        return url_for('calculate/', url = "efsefsefsef" )

    return render_template("index.html")




@app.route('/calculate/<url>')
def calculate(url):
    html_content = scrape(url)
    list_words = get_list_words(html_content)

    counts = Counter(list_words)
    return counts

if __name__ == '__main__':
    app.run(debug=True)