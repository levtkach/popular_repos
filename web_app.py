from flask import Flask, request, render_template_string
from github_api import fetch_repositories
from utils import sort_repositories_by_stars
from config import GITHUB_TOKEN

app = Flask(__name__)


@app.route("/")
def index():
    query = request.args.get("q", "telegram")
    try:
        repos = fetch_repositories(query, GITHUB_TOKEN)
        top10 = sort_repositories_by_stars(repos)[:10]
    except Exception as e:
        return f"<p>Error: {e}</p>"

    return render_template_string(
        """
        <h2>Топ 10 GitHub Repos для '{{ query }}'</h2>
        <ul>
            {% for repo in repos %}
                <li>
                    <a href="{{ repo['html_url'] }}">{{ repo['name'] }}</a> (⭐ {{ repo['stargazers_count'] }})
                </li>
            {% endfor %}
        </ul>
        <form>
            <input name="q" placeholder="Поиск" />
            <button type="submit">Поиск</button>
        </form>
    """,
        repos=top10,
        query=query,
    )


if __name__ == "__main__":
    app.run(debug=True)
