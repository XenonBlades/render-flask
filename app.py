from fkask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<h1>Ayush FLask</h1>"

if __name__ == "__main__":
    app.run()
