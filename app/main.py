import os
import sqlite3
from pathlib import Path
from flask import Flask, jsonify, request

DB_PATH = os.environ.get("DB_PATH", "/tmp/cloud_tasks.db")


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(DATABASE=DB_PATH)
    if test_config:
        app.config.update(test_config)

    def connect():
        path = Path(app.config["DATABASE"])
        path.parent.mkdir(parents=True, exist_ok=True)
        db = sqlite3.connect(str(path))
        db.row_factory = sqlite3.Row
        return db

    with connect() as db:
        db.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, done INTEGER NOT NULL DEFAULT 0)")
        db.commit()

    @app.get("/")
    def index():
        return jsonify(service="cloud-tasks-api", message="API de tarefas em nuvem", endpoints=["/health", "/tasks"])

    @app.get("/health")
    def health():
        try:
            with connect() as db:
                db.execute("SELECT 1").fetchone()
            return jsonify(status="ok"), 200
        except sqlite3.Error:
            return jsonify(status="error"), 503

    @app.get("/tasks")
    def list_tasks():
        with connect() as db:
            items = db.execute("SELECT id, title, done FROM tasks ORDER BY id").fetchall()
        return jsonify([dict(id=r["id"], title=r["title"], done=bool(r["done"])) for r in items])

    @app.post("/tasks")
    def create_task():
        data = request.get_json(silent=True)
        if not isinstance(data, dict) or not isinstance(data.get("title"), str) or not data["title"].strip():
            return jsonify(error="title deve ser texto nao vazio"), 400
        title = data["title"].strip()
        if len(title) > 120:
            return jsonify(error="title excede 120 caracteres"), 400
        with connect() as db:
            cursor = db.execute("INSERT INTO tasks(title) VALUES (?)", (title,))
            db.commit()
            task_id = cursor.lastrowid
        return jsonify(id=task_id, title=title, done=False), 201

    @app.patch("/tasks/<int:task_id>")
    def update_task(task_id):
        data = request.get_json(silent=True)
        if not isinstance(data, dict) or type(data.get("done")) is not bool:
            return jsonify(error="done deve ser booleano"), 400
        with connect() as db:
            cursor = db.execute("UPDATE tasks SET done=? WHERE id=?", (int(data["done"]), task_id))
            db.commit()
        if not cursor.rowcount:
            return jsonify(error="tarefa nao encontrada"), 404
        return jsonify(id=task_id, done=data["done"]), 200

    return app


app = create_app()
