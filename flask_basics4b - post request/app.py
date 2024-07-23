from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit_data', methods=['POST'])
def submit_data():
    name = request.form.get('name')
    age = request.form.get('age')
    email = request.form.get('email')
    password = request.form.get('password')
    return render_template('display.html', name=name, age=age, \
                           email=email, password=password)

if __name__ == '__main__':
    app.run(debug=True, port=8888)
    
# get requests and posts requests
