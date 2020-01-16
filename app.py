from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def getValue():
    threePointFG = request.form['threeFG']
    return render_template('result.html', three=threePointFG)

if __name__ == "__main__":
    app.run()
