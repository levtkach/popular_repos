import argparse
from github_api import fetch_repositories
from utils import sort_repositories_by_stars, save_to_json
from config import GITHUB_TOKEN


def main():
    parser = argparse.ArgumentParser(
        description="Get top GitHub repositories by keyword"
    )
    parser.add_argument("query", type=str, help="Search keyword (e.g., telegram)")
    args = parser.parse_args()

    try:
        repos = fetch_repositories(args.query, GITHUB_TOKEN)
        top10 = sort_repositories_by_stars(repos)[:10]

        for repo in top10:
            print(f"Name: {repo['name']}")
            print(f"URL: {repo['html_url']}")
            print(f"Stars: {repo['stargazers_count']}\n")

        save_to_json(top10)
        print("✅ Результаты сохранены в popular_repos.json")

    except Exception as e:
        print(f"❌ Ошибка: {e}")


if __name__ == "__main__":
    main()
