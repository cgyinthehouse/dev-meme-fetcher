import os
import re
import requests
from dotenv import load_dotenv

readme = os.path.abspath("README.md")


def update_meme(new_url):
    with open(readme, "r+", encoding="utf-8") as md:
        lines = md.readlines()

        # Replace the src value
        for i, line in enumerate(lines):
            if 'alt="Reddit"' in line:
                lines[i] = re.sub(r'src="(.+?)"', f'src="{new_url}"', line)
                break

        md.seek(0)
        md.writelines(lines)


def comment_area():
    with open(readme, "r", encoding="utf-8") as rd:
        lines = rd.readlines()

    # Find the start line of the meme comment block
    for i, line in enumerate(lines):
        if "<!--MEME" in line:
            startline = i
            break

    # Find the end line of the meme comment block
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
    with open(readme, "r+", encoding="utf-8") as rd:
        lines = rd.readlines()
        lines = lines[:startline+1] + images + lines[startline+1:]
        rd.seek(0)
        rd.writelines(lines)


def is_urls_empty():
    start, end = comment_area()
    return start + 1 == end


def fetch_memes():
    # TODO: pass argument to set the amount

    # I set the amount to 100 per fetch
    url = "https://vvgskppmennronkqbstj.supabase.co/rest/v1/memes?select=*&offset=0&limit=10&order=id.asc"

    load_dotenv()
    headers = {"apikey": os.getenv("apikey")}

    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        print(data)
        print('\nResponse status code: ', response.status_code)
        return None


def extract_url():
    start, _ = comment_area()
    with open(readme, 'r+', encoding='utf-8') as rd:
        lines = rd.readlines()
        url = lines.pop(start + 1)
        rd.seek(0)
        rd.writelines(lines)

    return url.replace("\n", '')
