from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/panda')
def panda():
    return render_template('pandas.html')

@app.route('/chicken')
def chicken():
    return render_template('chicken.html')

if __name__ == '__main__':
    app.run(debug=True)
