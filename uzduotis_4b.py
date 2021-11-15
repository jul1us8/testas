from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])

def home():
    if request.method == "POST":
        metai = int(request.form["metai"])

        if (metai % 4) == 0 and (metai % 100) == 0 and (metai % 400) == 0:
            return render_template("uzduotis_4b_keliamieji.html", metai = metai)

        elif (metai % 4) == 0 and (metai % 100) != 0:
            return render_template("uzduotis_4b_keliamieji.html", metai = metai)

        else:
            return render_template("uzduotis_4b_input.html")


    else:
        return render_template("uzduotis_4b_input.html")

if __name__ == "__main__":
    app.run()