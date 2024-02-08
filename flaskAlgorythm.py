from flask import Flask, request, render_template
from scraper import getInnerHTML, scrapeVids, pandas_output

import time

global flLinkInput
global start_time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # user_variable = request.form['user_variable']
        input = request.form["flLinkInput"]
        try:
            start_time = time.time()
            innerHTML = getInnerHTML(input)
        except:
            errorUrl = "GO BACK AND ENTER VALID URL !!!"
            print(errorUrl)
            return render_template("error.html", err=errorUrl)
        else:
            print("getting Inner HTML successfuly :)")
        try:
            playlist = scrapeVids(innerHTML)
        except:
            errorScr = "SCRAPPER ERROR, GO BACK AND TRY AGAIN !!!"
            print(errorScr)
            return render_template("error.html", err=errorScr)
        else:
            duration = time.time() - start_time
            print("scrapping successfuly :)")
            print(f"Duration: {duration}")
        return render_template("index2.html", playlist = playlist)
        # return user_variable
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
