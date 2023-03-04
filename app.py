
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuração do MySQL
app.config['MYSQL_HOST'] = 'opensourcelinux.tech'
app.config['MYSQL_USER'] = 'iago'
app.config['MYSQL_PASSWORD'] = 'eduardaamor15'
app.config['MYSQL_DB'] = 'dbcasa'

mysql = MySQL(app)

# Função para inserir os dados na tabela
def inserir_dados(data, valor, descricao, categoria):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO sz_gastos (id, data, valor, descricao, categoria) VALUES (%s, %s, %s, %s, %s)", (None,data, valor, descricao, categoria))
    mysql.connection.commit()
    cur.close()

# Rota para inserir os dados na tabela
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']
        valor = request.form['valor']
        descricao = request.form['descricao']
        categoria = request.form['categoria']
        inserir_dados(data, valor, descricao, categoria)
        cur = mysql.connection.cursor()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sz_gastos")
    dados = cur.fetchall()
    cur.close()
    total = sum([float(d[3]) for d in dados])
    return render_template('index.html', dados=dados, total=total)

# Rota para exibir os dados em uma lista
@app.route('/lista')
def lista():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sz_gastos")
    dados = cur.fetchall()
    cur.close()
    total = sum([float(d[3]) for d in dados])
    return render_template('lista.html', dados=dados, total=total)

if __name__ == '__main__':
    app.run(debug=True)
