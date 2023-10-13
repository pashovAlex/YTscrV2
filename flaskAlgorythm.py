from flask import Flask, request, render_template
from scraper import getInnerHTML, scrapeUrls, pandas_output

global flLinkInput
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # user_variable = request.form['user_variable']
        return render_template("index2.html", urls = scrapeUrls(getInnerHTML(request.form['flLinkInput'])), i = 1)
        # return user_variable
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
