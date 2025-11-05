from flask import jsonify
from conexao import get_conexao
from psycopg2.extras import RealDictCursor

def buscar_tarefas():
    con = get_conexao()
    cursor = con.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, name, description FROM todos"
    )

    todos = cursor.fetchall()

    cursor.close()
    con.close()

    return jsonify(todos)

def buscar_tarefa(id):
    con = get_conexao()
    cursor = con.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, name, description FROM todos WHERE id = %s",
        (id,)
    )

    todo = cursor.fetchone()

    cursor.close()
    con.close()

    return jsonify(todo)