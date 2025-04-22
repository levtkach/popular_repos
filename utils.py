import json

def sort_repositories_by_stars(repos: list) -> list:
    return sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)

def save_to_json(data: list, filename: str = "popular_repos.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
