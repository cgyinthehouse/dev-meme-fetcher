## Dev memes for README

<!-- Syntax that is able to resize images on Github's markdown -->
<p align="center"><img alt="MEME" src="https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(49).jpgdev-memes.com460dbd72-0f58-4860-a25e-c3e6eaf3b105" width="30%" /></p>

This action gets a list of dev meme image URLs to a comment block in the README.md, it will replace the image src field with the first url list in the comment block when it runs. When it comes to an empty list in the comment block, this action will get a new one.

---

## Usage

Just place an `img` tag with `alt="MEME"` in your README, for example `<img alt="MEME" />`, you can also set the width or height if you want to.

If you want to set the amount of URLs that saved to the comment block, you can set the `fetch_num`. The default is 100.
You can optionally set the commit author and email with `commit_author` and `commit_email`.

**(NOTICE‼️)** In order to let this action modify the README, make sure you have enabled the "***Read and write permissions***" under the "***Workflow permissions***" in your repository settings.

### Example Workflow

```yaml
name: Dev Memes
on:
  # run on every 24 hours
  schedule:
    - cron: '0 */24 * * *'
      
  # or run on every push on the master branch 
  push:
    branches:
    - master
    
jobs:
  deploy:
    name: Update Dev Meme
    runs-on: ubuntu-latest
    steps:
      - name: Update meme
        uses: cgyinthehouse/dev-memes-for-README@v1.0
        with:
          fetch_num: 50
          commit_author: Mike Oxlong
          commit_email: mikeoxlong@users.noreply.github.com
```



---

#### TODO
- [x] ~~Automatically create meme comment block.~~
- [ ] Maybe set the image size from Actions?
- [ ] For diversity, host a meme api server or randomize the list from the api
- [ ] Make the meme comment block optional

<!--MEME
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(50).jpgdev-memes.com409dbf0d-5e60-49dd-aec3-7a0d7bfd202f
-->
