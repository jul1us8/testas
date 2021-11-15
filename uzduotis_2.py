from flask import Flask

app = Flask(__name__)

@app.route("/<kintamasis>")
def home(kintamasis):
    return f"{kintamasis} {kintamasis} {kintamasis} {kintamasis} {kintamasis}"

if __name__ == "__main__":
    app.run()