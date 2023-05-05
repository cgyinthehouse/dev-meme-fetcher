from utils import insert_urls, update_meme, is_urls_empty, fetch_memes

# Fetching and insertion is available only if the comment block is empty
if is_urls_empty():
    insert_urls(fetch_memes())

update_meme()
