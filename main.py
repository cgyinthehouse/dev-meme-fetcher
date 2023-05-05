from utils import insert_urls, update_meme, is_urls_empty, fetch_memes, extract_url

# Fetching and insertion is available only if the comment block is empty
if is_urls_empty():
    urls = fetch_memes()
    insert_urls(urls)

update_meme(extract_url())


"""
TODO:
    Put the image url list in the comment block in the README,
    when we are going to update the src field, grap one url from the comment
    and replace the field, then move the comment mark "<!--" down.

    If the url list in the comment block is empty, refetch a new one and insert
    into it.

    The consumption speed of the meme urls is depending on the cron setting on
    Github Action of the user.
"""
