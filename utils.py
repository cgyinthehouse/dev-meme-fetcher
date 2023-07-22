import os
import re
import requests

readme = os.path.abspath("README.md")


def update_meme():
    start, _ = comment_area()
    if not start:
        return

    with open(readme, "r", encoding="utf-8") as md:
        lines = md.readlines()

    # Extract the url from meme comment block
    url = lines.pop(start + 1).replace("\n", "")

    # Replace the src value
    for i, line in enumerate(lines):
        if match := re.search(r'<img\s[^>]*alt="MEME"[^>]*>', line):
            if "src=" not in match.group():
                line = line.replace("<img", '<img src=""')
            lines[i] = re.sub(r'src="([^"\s]*)"', f'src="{url}"', line)
            break

    with open(readme, "w+", encoding="utf-8") as rd:
        rd.writelines(lines)


def comment_area() -> tuple[int | None, int | None]:
    with open(readme, "r", encoding="utf-8") as rd:
        lines = rd.readlines()

    # Find the start line of the meme comment block
    startline, endline = None, None
    for i, line in enumerate(lines):
        if "<!--MEME" in line:
            startline = i
            break

    # Find the end line of the meme comment block
    if startline:
        for i, line in enumerate(lines[startline:]):
            if line.strip() == "-->":
                endline = startline + i
                break

    return startline, endline


def create_comment():
    with open(readme, "r", encoding="utf-8") as rd:
        lines = rd.readlines()
    # add the comment to end line
    lines = lines + ["<!--MEME\n", "-->\n"]

    with open(readme, "w+", encoding="utf-8") as md:
        md.writelines(lines)


def insert_urls(data):
    if data is None:
        return

    images = []
    d = "https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/"

    for i in data:
        href = i["href"].replace(" ", "%20")
        images.append(d + href + "\n")

    startline, _ = comment_area()
    with open(readme, "r", encoding="utf-8") as rd:
        lines = rd.readlines()
        if startline:
            lines = lines[: startline + 1] + images + lines[startline + 1 :]

    with open(readme, "w+", encoding="utf-8") as md:
        md.writelines(lines)


def is_urls_empty():
    start, end = comment_area()
    if start and end:
        return start + 1 == end
    else:
        create_comment()
        return True


def fetch_memes(limit: int = 100):
    url = "https://sore-puce-octopus-shoe.cyclic.app/api"
    response = requests.get(url, params={"limit": limit})
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        print(data)
        print("\nResponse status code: ", response.status_code)
        return None
