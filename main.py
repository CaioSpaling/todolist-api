from flask import Flask, request
from tarefa import buscar_tarefas, buscar_tarefa, criar_tarefa, apagar_tarefa, editar_tarefa

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return {
        'message': 'Api rodando'
    }

@app.route('/api/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = buscar_tarefas()
    return tarefas

@app.route('/api/tarefa/<int:todo_id>', methods=['GET'])
def get_tarefa(todo_id):
    tarefa = buscar_tarefa(todo_id)
    return tarefa

@app.route('/api/tarefas', methods=['POST'])
def create_tarefa():
    corpo = request.get_json()
    tarefa_name = corpo.get('name')
    tarefa_desc = corpo.get('description')
    criar_tarefa(tarefa_name, tarefa_desc)
    return {
        'message': 'Tarefa cadastrada com sucesso, lindinho!'
    }

@app.route('/api/tarefas/<int:tarefa_id>', methods=['DELETE'])
def delete_tarefa(tarefa_id):
    apagar_tarefa(tarefa_id)
    return {
        'message': 'Tarefa apagado com sucesso, lindinho!'
    }
    
@app.route('/api/tarefas/<int:tarefa_id>', methods=['PUT'])
def edit_tarefa(tarefa_id):
    corpo = request.get_json()
    tarefa_name = corpo.get('name')
    tarefa_desc = corpo.get('description')
    editar_tarefa(tarefa_id, tarefa_name, tarefa_desc)
    return {
        'message': 'Tarefa atualizada com sucesso, lindinho!'
    }

if __name__ == '__main__':
    app.run(debug=True)