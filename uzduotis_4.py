from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])

def home():
    if request.method == "POST":
        metai = int(request.form["metai"])

        if (metai % 4) == 0 and (metai % 100) == 0 and (metai % 400) == 0:
            return render_template("uzduotis_4.html", keliamieji = True, metai = metai)

        elif (metai % 4) == 0 and (metai % 100) != 0:
            return render_template("uzduotis_4.html", keliamieji = True, metai = metai)

        else:
            return render_template("uzduotis_4.html", keliamieji = False)


    else:
        return render_template("uzduotis_4.html", keliamieji = False)

if __name__ == "__main__":
    app.run()
