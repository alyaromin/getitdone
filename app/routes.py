from flask import render_template, redirect, url_for, request, flash
from app import app, db
from sqlalchemy import text


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_connection')
def check_connection():
    try:
        # Пытаемся выполнить простой запрос к базе данных
        db.session.execute(text("SELECT 1"))
        return "Подключение к базе данных успешно!"
    except Exception as e:
        return f"Ошибка подключения: {e}"
