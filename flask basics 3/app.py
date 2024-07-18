from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Type some text as an endpoint to analyse it'

@app.route('/<text>')
def analyse(text):
    # get length
    length = len(text)

    # get number of digits and vowels
    num_digits = 0
    num_vowels = 0
    for char in text:
        if char.isdigit():
            num_digits += 1
        if char.lower() in 'aeiou':
            num_vowels += 1

    # get letter frequency
    letter_freq = {} # initialise empty dictionary
    for char in text:
        char = char.lower()
        if char not in letter_freq:
            letter_freq[char] = 1
        else: # char exists in dictionary
            letter_freq[char] += 1

    return render_template('analysis.html', text=text, length=length, num_digits=num_digits, \
                           num_vowels=num_vowels, letter_freq=letter_freq)
        
if __name__ == '__main__':
    app.run(debug=True, port=7777)
