from flask import Flask, render_template, request
from model import predictRating
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def getValue():
    threeP = None
    threeAcc = None
    twoP = None
    twoAcc = None
    ft = None
    ftAcc = None
    trb = None
    ast = None
    blk = None
    if (request.form['threeFG'] == ""):
        threeP = 0
    else:
        threeP = float(request.form['threeFG'])

    if (request.form['threeAcc'] == ""):
        threeAcc = 0
    else:
        threeAcc = float(request.form['threeAcc'])

    if (request.form['twoFG'] == ""):
        twoP = 0
    else:
        twoP = float(request.form['twoFG'])

    if (request.form['twoAcc'] == ""):
        twoAcc = 0
    else:
        twoAcc = float(request.form['twoAcc'])

    if (request.form['freeThrow'] == ""):
        ft = 0
    else:
        ft = float(request.form['freeThrow'])

    if (request.form['ftAcc'] == ""):
        ftAcc = 0
    else:
        ftAcc = float(request.form['ftAcc'])

    if (request.form['rebound'] == ""):
        trb = 0
    else:
        trb = float(request.form['rebound'])

    if (request.form['assist'] == ""):
        ast = 0
    else:
        ast = float(request.form['assist'])

    if (request.form['block'] == ""):
        blk = 0
    else:
        blk = float(request.form['block'])

    rating = predictRating(threeP, threeAcc, twoP, twoAcc, ft, ftAcc, trb, ast, blk)
    return render_template('result.html', rating=round(rating[0], 3))


if __name__ == "__main__":
    app.run()
