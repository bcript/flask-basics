# file can be called main.py/app.py
from flask import Flask, render_template  # import class Flask
import random

app = Flask(__name__)  # create instance of that class

my_college = 'ASRJC'
rival_college = 'ACJC'
secret_text = 'Goblin is stinky'
secret_nums = [1111, 2222, 1234567890]
secret_info = {'name': 'Basil', 'description': 'stupid', 'gender': 'Goblin', 'type': 'Uncommon'}

@app.route('/')  # @ is a decorator
def home():
    return "<h1>HELLO!</h1><p>This is my page</p>"

@app.route('/bestsubject')
@app.route('/computersubject')
@app.route('/h2computing')
@app.route('/computing')
def computing(): 
    return '''<h1>What is computing?</h1>
            <h2>Computing is a subject</h2>
            '''

@app.route('/about')
def about():
    return render_template('about.html', my_college=my_college, rival_college=rival_college)

@app.route('/secret')
def secret():
    lucky_num = random.choice(secret_nums)
    return render_template('secret.html', secret_text=secret_text, secret_nums=secret_nums, secret_info=secret_info, lucky_num=lucky_num)

if __name__ == '__main__':
    app.run(debug=True)   # any port can be used, as long as 4-5 digits
