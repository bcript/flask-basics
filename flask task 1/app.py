from flask import Flask, render_template, url_for, request

app = Flask(__name__)
contacts = []

@app.route('/', methods=['GET', 'POST'])
def home():
        if request.method == 'POST':
                name = request.form.get('name')
                number = request.form.get('number')
                email = request.form.get('email')
                contacts.append({'name': name, 'number': number, 'email': email})
        return render_template('index.html', contacts=contacts)

if __name__ == '__main__':
        app.run(debug=True, port=1111)
