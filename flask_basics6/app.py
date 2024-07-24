from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)
messages = []

@app.route('/', methods=['GET', 'POST'])
def home():
        if request.method == 'POST':
                message = request.form.get('message')
                author = request.form.get('author')
                # file closes after with block
                with open('messages.txt', 'a') as file:
                        file.write(message + '\n')
                messages.append({'message': message, 'author': author})

                # connect to SQL DB
                connection = sqlite3.connect('messages.db')
                cursor= connection.cursor()

                cursor.execute('INSERT INTO users (message, author) VALUES (?, ?)', (message, author))
                connection.commit()
                connection.close()
                return redirect('/')
                
        else: # GET request
                return render_template('index.html', messages=messages)
        
if __name__ == '__main__':
    app.run(debug=True,  port=1111)
