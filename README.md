# 🔎 Популярные GitHub-репозитории по ключевому слову

Простое CLI-приложение на Python, которое ищет **10 самых популярных репозиториев** на GitHub по заданному ключевому слову, **сортирует их по количеству звёзд** и сохраняет результат в **JSON-файл**.

---

## 🚀 Быстрый старт

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/popular_repos.git
   cd popular_repos

2. Создайте и активируй виртуальное окружение:
   ```bash
    python3 -m venv venv
    source venv/bin/activate

3. Установите зависимости:
   ```bash
    pip install -r requirements.txt

4. Добавьте GitHub-токен в .env:
   ```bash
    GITHUB_TOKEN=ghp_твой_токен_здесь

5. Запустите приложение:
   ```bash
    python main.py
