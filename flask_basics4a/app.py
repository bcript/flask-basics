from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit_data')
def submit_data():
    name = request.args.get('name')
    age = request.args.get('age')
    email = request.args.get('email')
    password = request.args.get('password')
    return render_template('display.html', name=name, age=age, \
                           email=email, password=password)

if __name__ == '__main__':
    app.run(debug=True, port=7777)
    
# get requests and posts requests
