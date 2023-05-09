## Dev memes for README

This action gets a list of dev meme image URLs to a comment block in the README.md, it will replace the image src field with the first url list in the comment block when it runs. When it comes to an empty list in the comment block, this action will get a new one.

Just place an `img` tag with `alt="MEME"` in your README, you can also set the width or height if you want to.
For instance `<img alt="MEME" src="" width="350"/>`.

Because the github markdown doesn't have a way to resize the image(or there are but I just don't know), so you have to use the `img` tag in your README.md to adjust the image size.

If you want to set the amount per fetch, you can set the `fetch_num`. The default is 100.

---

## Usage

Github Actions

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
```

### Notice

Make sure you have enabled the **Read and write permissions** in the **Workflow permissions** setting of your repo to have this action work.
Go to the repo setting and select *Actions* > *General* at the sidebar, you will see the options at the bottom section of the page.

<!-- Syntax that is able to resize images on Github's markdown -->
<img alt="MEME" src="https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(5).jpgdev-memes.com2c1f03f5-6d6a-4328-bdec-ab73811eecde" width="300" />

#### TODO
- [ ] ~~Automatically create meme comment block.~~
- [ ] Maybe set the image size from Actions?

<!--MEME
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(6).jpgdev-memes.comb9c9dc43-717c-4d8e-83eb-f70b2c88dd9e
-->
