# noinspection PyUnresolvedReferences
from flask import Flask
# noinspection PyUnresolvedReferences
from flask import render_template
# noinspection PyUnresolvedReferences
from flask import request

app = Flask(__name__)


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
    )


app.run(debug=True)
