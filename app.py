from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Caminho da base de dados partilhada (pasta pai)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'banco.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabelas():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inscricoes (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            nome             TEXT NOT NULL,
            data_nascimento  TEXT NOT NULL,
            fotografia       TEXT,
            morada           TEXT NOT NULL,
            encarregado      TEXT NOT NULL,
            contacto         TEXT NOT NULL,
            email            TEXT NOT NULL,
            classe           TEXT NOT NULL,
            curso            TEXT NOT NULL,
            turma            TEXT NOT NULL,
            turno            TEXT NOT NULL,
            historico        TEXT NOT NULL,
            situacao         TEXT DEFAULT 'Pendente',
            pagamento        TEXT,
            data_pagamento   TEXT,
            descricao        TEXT,
            valor            TEXT,
            status_pagamento TEXT DEFAULT 'Pendente',
            data_inscricao   TEXT DEFAULT (date('now'))
        )
    ''')
    conn.commit()
    conn.close()

criar_tabelas()

# Página inicial (apresentação)
@app.route('/')
def index():
    return render_template('index.html')

# Formulário de inscrição
@app.route('/inscricao')
def inscricao():
    return render_template('inscricao.html')

# Guardar inscrição
@app.route('/salvar', methods=['POST'])
def salvar():
    dados = request.form

    # Tratar fotografia (nome do ficheiro se enviado)
    foto = request.files.get('fotografia')
    nome_foto = ''
    if foto and foto.filename != '':
        upload_dir = os.path.join(app.root_path, 'static', 'fotos')
        os.makedirs(upload_dir, exist_ok=True)
        nome_foto = foto.filename
        foto.save(os.path.join(upload_dir, nome_foto))

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO inscricoes (
            nome, data_nascimento, fotografia, morada, encarregado,
            contacto, email, classe, curso, turma, turno, historico,
            situacao, pagamento, data_pagamento, descricao, valor, status_pagamento
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        dados.get('nome'),
        dados.get('data_nascimento'),
        nome_foto,
        dados.get('morada'),
        dados.get('encarregado'),
        dados.get('contacto'),
        dados.get('email'),
        dados.get('classe'),
        dados.get('curso'),
        dados.get('turma'),
        dados.get('turno'),
        dados.get('historico'),
        'Pendente',
        dados.get('pagamento'),
        dados.get('data_pagamento'),
        dados.get('descricao'),
        dados.get('valor'),
        dados.get('status_pagamento', 'Pendente')
    ))
    conn.commit()
    conn.close()

    return redirect(url_for('sucesso'))

# Página de sucesso
@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
