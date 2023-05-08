import os
import re
import requests
from dotenv import load_dotenv

readme = os.path.abspath("README.md")


def update_meme():
    start, _ = comment_area()
    if not start:
        return

    with open(readme, "r", encoding='utf-8') as md:
        lines = md.readlines()

    # Extract the url from meme comment block
    url = lines.pop(start + 1).replace('\n', '')

    # Replace the src value
    for i, line in enumerate(lines):
        if 'alt="Reddit"' in line:
            lines[i] = re.sub(r'src="(.+?)"', f'src="{url}"', line)
            break

    with open(readme, 'w+', encoding='utf-8') as rd:
        rd.writelines(lines)


def comment_area() -> tuple[int|None, int|None]:
    with open(readme, "r", encoding="utf-8") as rd:
        lines = rd.readlines()

    # Find the start line of the meme comment block
    startline, endline = None,None
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


def insert_urls(data):
    if data is None:
        return

    images = []
    d = "https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/"

    for i in data:
        href = i["href"].replace(" ", "%20")
        images.append(d + href + "\n")

    startline, _ = comment_area()
    with open(readme, "r", encoding='utf-8') as rd:
        lines = rd.readlines()
        if startline:
            lines = lines[:startline+1] + images + lines[startline+1:]

    with open(readme, 'w+', encoding='utf-8') as md:
        md.writelines(lines)


def is_urls_empty():
    start, end = comment_area()
    if start and end:
        return start + 1 == end
    else:
        raise Exception("Can't find the MEME mark in the comment")


def fetch_memes(limit:int|str = 100):
    # the amount is 100 per fetch by default
    url = f"https://vvgskppmennronkqbstj.supabase.co/rest/v1/memes?select=*&offset=0&limit={limit}&order=id.asc"

    load_dotenv()
    if apikey := os.getenv("apikey"):
        headers = {"apikey": apikey}
    else:
        raise Exception("apikey not found")

    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        print(data)
        print('\nResponse status code: ', response.status_code)
        return None
