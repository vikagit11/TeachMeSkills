# 🗳️ Flask Опросник — Простой сервис голосований

Этот проект — учебное приложение на Flask. Позволяет создавать опросы с вариантами ответов, голосовать и удалять опросы.

---

## 🚀 Быстрый запуск (шаг за шагом)

### 1. Клонируй проект

```bash
git clone https://github.com/yourname/flask-polls.git
cd flask-polls

2. Создай и активируй виртуальное окружение

python3 -m venv venv
source venv/bin/activate      # для Mac/Linux

3. Установи зависимости

pip install -r requirements.txt

4. Создай файл .env

Создай файл .env в корне проекта и вставь туда:

DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/polls_db
SECRET_KEY=supersecretkey




⸻

🏃 Запуск приложения

python run.py

Перейди в браузере: http://127.0.0.1:5000

⸻

🔧 Что умеет приложение
	•	Главная страница со списком всех опросов
	•	Создание новых опросов с 2–5 вариантами ответов
	•	Голосование за варианты без авторизации
	•	Просмотр количества голосов
	•	Удаление опросов

⸻

⚙️ Используемые технологии
	•	Flask
	•	PostgreSQL
	•	SQLAlchemy
	•	Alembic
	•	Flask-WTF
	•	Jinja2
	•	HTML + Bootstrap

⸻

💡 Команды миграций (если изменишь модели)

Создание миграции:

alembic revision --autogenerate -m "новые поля"

Применение миграции:

alembic upgrade head

📁 Структура проекта

polls_app/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── poll_detail.html
│       └── create_poll.html
├── static/
├── migrations/
├── .env
├── .gitignore
├── alembic.ini
├── config.py
├── requirements.txt
├── run.py
└── README.md

🧑‍💻 Автор

Учебный проект от TeachMeSkills.by
Сделано с ❤️ на Flask.
