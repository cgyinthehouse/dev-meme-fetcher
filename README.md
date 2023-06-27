## Dev memes for README

This action gets a list of dev meme image URLs to a comment block in the README.md, it will replace the image src field with the first url list in the comment block when it runs. When it comes to an empty list in the comment block, this action will get a new one.

Just place an `img` tag with `alt="MEME"` in your README, you can also set the width or height if you want to.
For instance `<img alt="MEME" src="" width="350"/>`.

Because the `![exmaple](https://exampleimage.png)` syntax doesn't have a way to resize the image on github (or there are but I just don't know), so you have to use the `img` tag in your README.md to adjust the image size.

If you want to set the amount of URLs that saved to the comment block, you can set the `fetch_num`. The default is 100.
You can optionally change the commit author and email by setting `commit_author` and `commit_email`. This will default to *github-actions* and *github-actions@github.com*

---

## Usage

Example Workflow

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
          commit_author: Kent Chen
          commit_email: cgyinthehouse@github.com
```

### Notice

Make sure you have enabled the "***Read and write permissions***" in the "***Workflow permissions***" setting of your repo to have this action work.
Go to the repo setting and select *Actions* > *General* at the sidebar, you will see the options at the bottom section of the page.

---
<!-- Syntax that is able to resize images on Github's markdown -->
<img alt="MEME" src="https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(44).jpgdev-memes.com333c835e-f181-4b58-8b34-66440a3b893f" width="450" />

#### TODO
- [x] ~~Automatically create meme comment block.~~
- [ ] Maybe set the image size from Actions?
- [ ] For diversity, host a meme api server or randomize the list from the api
- [ ] Make the meme comment block optional

<!--MEME
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(45).jpgdev-memes.com7d9c88bf-c1ec-4409-89f2-22bddcf0eb65
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(46).jpgdev-memes.combd501cee-aab1-46d5-a40a-58acc875d57c
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(47).jpgdev-memes.com9fa9d0b8-d311-45d2-a96e-41604d313eae
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(48).jpgdev-memes.comff9e67c0-b83d-4175-8a32-d0c78833077b
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(49).jpgdev-memes.com460dbd72-0f58-4860-a25e-c3e6eaf3b105
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(50).jpgdev-memes.com409dbf0d-5e60-49dd-aec3-7a0d7bfd202f
-->
