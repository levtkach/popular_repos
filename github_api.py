import requests
import os


def fetch_repositories(query: str, token: str | None = None):
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"
    headers = {"Authorization": f"token {token}"} if token else {}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["items"]
