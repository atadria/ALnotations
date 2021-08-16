from flask import Flask, render_template, request

from model.model import NERModel

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=["POST"])
def process():
    if request.method == 'POST':
        language = request.form['languageoption']
        rawtext = request.form['rawtext']
        nlp = NERModel(language)
        results = [(ent.label_, ent.text) for ent in nlp.predict(rawtext)]
        num_of_results = len(results)

    return render_template("index.html", results=results, num_of_results=num_of_results)


if __name__ == '__main__':
    app.run(debug=True)
