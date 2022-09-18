# noinspection PyUnresolvedReferences
from flask import Flask
# noinspection PyUnresolvedReferences
from flask import render_template
# noinspection PyUnresolvedReferences
from flask import request
import random

app = Flask(__name__)


@app.route("/")
@app.route('/home')
def home():
    return """
    <a href="/exersice">exersice</a><br>
    <a href="/index">index</a><br>
    """


@app.route('/exersice', methods=['GET', 'POST'])
def exersice():
    text = ""
    result = ""
    if request.method == 'POST':
        text = request.form.get('input_text')
        max_s = 0
        max_len = 0
        max_str = ""
        for line in text.split("\n"):
            if str(line).count("S") > max_s or str(line).count("S") == max_s and len(line) > max_len:
                max_str = line
                max_len = len(line)
                max_s = line.count("S")
        result = max(max_str.split("S"), key=lambda x: len(x))
        print(text, result, sep="\n\n")
    return render_template(
        "exersice.html",
        input=text,
        output=result,
        num=random.randint(0, 3),
    )


@app.route('/index')
def index():
    images = {
        "cat1": {
            "text": "кот",
            "url": "https://thiscatdoesnotexist.com/"
        },
        "cat2": {
            "text": "рисунок",
            "url": "https://thisartworkdoesnotexist.com/"
        },
        "cat3": {
            "text": "лошадь",
            "url": "https://thishorsedoesnotexist.com/"
        },
        "c4": {
            "c2": "text"
        }
    }
    names = [
        "привет",
        "это самый лучший сайт",
        "как дела?",
        "не придумал("
    ]
    number = random.randint(0, 3)

    return render_template(
        "index.html",
        images=images,
        num=number,
        random=random.randint,
    )


app.run()
