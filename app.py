from lxml import html
import requests
import re
import urllib.request
from inscriptis import get_text
from flask import Flask
app = Flask(__name__)

def scrape():
    url = "https://www.bbc.co.uk"
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
    html_content = scrape()
    list_words = get_list_words(html_content)
    return list_words

if __name__ == '__main__':
    app.run(debug=True)