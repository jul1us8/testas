from flask import Flask, render_template

app = Flask(__name__)

@app.route("/keliamieji")
def home():
    visi_metai = list(range(1900, 2101))
    return render_template("uzduotis_3.html", visi_metai=visi_metai)

if __name__ == "__main__":
    app.run()