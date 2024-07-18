from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

# list of valid animals
valid_animals = ["chickens", "ducks", "pandas"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<animal>") # possible to take in more input/parameters
def animal_info(animal):
    if animal in valid_animals:
        return render_template(f"{animal}.html")
    else:
        return redirect(url_for("home"))
        
if __name__ == "__main__":
    app.run(debug=True, port=12345)
