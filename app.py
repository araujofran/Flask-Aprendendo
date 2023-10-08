from flask import Flask

app = Flask(__name__)

@app.route('/')

def homepage():
    return "<h1>Pagina Inicial</h1>"

app.run(debug=True)