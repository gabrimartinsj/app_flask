from flask import Flask, request, render_template # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template("index.html")

@app.route('/run', methods=['GET', 'POST'])
def run():
    if request.method == 'POST':
        if request.form['pass_value'] == 'Test':
            value ='Test just for fools and horses!'
            return render_template_string('''{{ value }}<br>''')
        elif request.form['pass_value'] == 'Test2':
            value ='Test2'
            return render_template_string('''{{ value }}<br>''')

if __name__ == '__main__':
    app.run(debug=True) # Executa a aplicação
