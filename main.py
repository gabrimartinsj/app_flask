import json
from flask import Flask, request, render_template, jsonify   # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True) # Executa a aplicação
