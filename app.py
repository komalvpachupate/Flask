from flask import Flask, render_template, request

from preprocess import preprocess
from keyphrase_extractor import candidate_keyword

app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return render_template('index.html')


@app.route('/', methods=['GET','POST'])
def keyword_extract():
    keyword_extract=[]
    if request.method == 'POST':
        text = request.form['text']
        clean_text = preprocess(text)
        candidate_words=candidate_keyword(clean_text)

        keyword_extract.append(candidate_words)

    return render_template('index.html',keyword_extract=keyword_extract)


if __name__== "__main__":
    app.run(debug=True)