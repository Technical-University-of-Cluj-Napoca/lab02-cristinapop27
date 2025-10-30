import sys
import requests
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) < 2:
        print("Usage: python define.py <word>")
        sys.exit(1)

    word = sys.argv[1]
    url = f"https://dexonline.ro/definitie/{word}"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching page: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.text, "html.parser")

    defs = soup.find("span", class_="tree-def html")

    if not defs:
        print(f"No definitions found for '{word}'.")
        sys.exit(0)

    text = defs.get_text(" ", strip=True)
    print(text)

if __name__ == "__main__":
    main()
