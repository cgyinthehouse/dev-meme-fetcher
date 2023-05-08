import sys
from utils import insert_urls, update_meme, is_urls_empty, fetch_memes

limit = sys.argv[1]

# Fetching and insertion is available only if the comment block is empty
if is_urls_empty():
    insert_urls(fetch_memes(limit))

update_meme()
