# Sistema Escolar – Complexo Escolar Privado Fonte de Saber

## Estrutura do Projeto

```
sistema_escolar/
├── banco.db                        ← Base de dados partilhada (criada automaticamente)
│
├── inscricao/                      ← App 1: Inscrição pública (porta 5000)
│   ├── app.py
│   └── templates/
│       ├── index.html              ← Página de apresentação
│       ├── inscricao.html          ← Formulário de inscrição
│       └── sucesso.html            ← Página de confirmação
│
├── gestao/                         ← App 2: Gestão interna (porta 5001)
│   ├── app.py
│   └── templates/
│       ├── login.html              ← Login + Cadastro de funcionários
│       ├── lista.html              ← Lista e gestão de inscrições
│       └── pagamentos.html         ← Gestão de pagamentos
│
└── api/                            ← App 3: API central (porta 5002)
    └── app.py
```

## Instalação

```bash
pip install flask
```

## Como Executar

Abre **3 terminais** separados:

**Terminal 1 – Inscrição (público):**
```bash
cd sistema_escolar/inscricao
python app.py
# Aceder em: http://localhost:5000
```

**Terminal 2 – Gestão (funcionários):**
```bash
cd sistema_escolar/gestao
python app.py
# Aceder em: http://localhost:5001
```

**Terminal 3 – API:**
```bash
cd sistema_escolar/api
python app.py
# Aceder em: http://localhost:5002
```

## Credenciais Padrão (Gestão)

- **Email:** admin@escola.com
- **Senha:** admin123

## Endpoints da API (porta 5002)

| Método | URL | Descrição |
|--------|-----|-----------|
| GET  | /api/inscricoes | Lista todas as inscrições |
| GET  | /api/inscricoes/:id | Detalhes de uma inscrição |
| PUT  | /api/inscricoes/:id/situacao | Atualiza situação |
| GET  | /api/pagamentos/:aluno_id | Pagamentos de um aluno |
| POST | /api/pagamentos | Registar pagamento |
| GET  | /api/stats | Estatísticas gerais |

---
Cread by: Shadow Walker!
