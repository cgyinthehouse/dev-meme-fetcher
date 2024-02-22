## Dev memes for README

<!-- Syntax that is able to resize images on Github's markdown -->
<p align="center"><img alt="MEME" src="https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(34).jpgdev-memes.com0b7bdb48-97df-4eb5-bacf-83a4af9c3eaa" width="30%" /></p>

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
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(35).jpgdev-memes.com7e977502-0d5f-4fc1-8d64-bfe1e45c4bba
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(36).jpgdev-memes.come93fcc4a-cf73-4f13-9a26-63a915d710f2
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(37).jpgdev-memes.comf2239120-0e2e-4727-93b3-68f5a5330967
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(38).jpgdev-memes.comc0db5a80-b6f7-499c-b89c-0e1637e0340c
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(39).jpgdev-memes.com1b9762f1-cad8-4469-9411-c3c2ef2ae325
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(40).jpgdev-memes.com5c72a531-a063-448c-87c9-b8d90df8f836
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(41).jpgdev-memes.comda84c1cc-47e5-40e0-b94f-d808f306cc32
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(42).jpgdev-memes.comeadc65a0-5fa4-4334-96a5-14746d696f97
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(43).jpgdev-memes.com90ab690c-2be9-4b1f-9355-c29b0174a6d9
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(44).jpgdev-memes.com333c835e-f181-4b58-8b34-66440a3b893f
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(45).jpgdev-memes.com7d9c88bf-c1ec-4409-89f2-22bddcf0eb65
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(46).jpgdev-memes.combd501cee-aab1-46d5-a40a-58acc875d57c
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(47).jpgdev-memes.com9fa9d0b8-d311-45d2-a96e-41604d313eae
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(48).jpgdev-memes.comff9e67c0-b83d-4175-8a32-d0c78833077b
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(49).jpgdev-memes.com460dbd72-0f58-4860-a25e-c3e6eaf3b105
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(50).jpgdev-memes.com409dbf0d-5e60-49dd-aec3-7a0d7bfd202f
-->
