from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<path:mockup>")
def sample(mockup):
    return render_template("{}.html".format(mockup))

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11536, debug=True)
