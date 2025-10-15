from flask import jsonify

def buscar_tarefas():
    tarefas = [
        {
            'id': 1,
            'nome': 'Aprender digitacao',
            'descricao': 'Vamos aumentar o zoom para enxergar',
            'status': 'Pendente'
        },
        {
            'id': 2,
            'nome': 'Aprender python',
            'descricao': 'Aprender python para fazer apis',
            'status': 'Pendente'
        }
    ]
    return jsonify(tarefas)

def buscar_tarefa():
    tarefa = {
            'id': 1,
            'nome': 'Aprender digitacao',
            'descricao': 'Vamos aumentar o zoom para enxergar',
            'status': 'Pendente'
    }
    return jsonify(tarefa)