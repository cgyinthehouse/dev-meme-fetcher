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
<img alt="MEME" src="https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(9).jpgdev-memes.comb560d4e1-4996-4f0a-84db-c1b5e5e4564a" width="450" />

#### TODO
- [x] ~~Automatically create meme comment block.~~
- [ ] Maybe set the image size from Actions?
- [ ] For diversity, host a meme api server or randomize the list from the api
- [ ] Make the meme comment block optional

<!--MEME
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(10).jpgdev-memes.com5f7c970c-65fe-47d3-98e9-22a86358dcad
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(11).jpgdev-memes.com49474f26-a768-4db2-90a5-60e1e44e5e89
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(12).jpgdev-memes.com0d6b0b7c-b360-4a25-a921-ae88f0235b16
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(13).jpgdev-memes.com41802917-9243-4204-baf3-44f73bf8ad4d
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(14).jpgdev-memes.com0fd58d49-b7a7-47db-b49d-f7da856b4cfa
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(15).jpgdev-memes.com00d715ca-c02d-476c-9f75-eb79ff801cb4
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(16).jpgdev-memes.com00124742-d96a-4eab-a814-e2bf297ba6be
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(17).jpgdev-memes.come7a597e3-58cb-42f6-bb86-99c9761e8621
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(18).jpgdev-memes.comc92a946c-a9f5-49c1-9a38-3844966df9e1
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(19).jpgdev-memes.comcf5135c1-2ed0-4b25-ba01-a7c5caf52473
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(20).jpgdev-memes.com74df42da-fd62-4023-979f-019b87daa522
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(1).jpgdev-memes.com34e1c4d8-e528-452e-b7d5-f419b52b1270
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(21).jpgdev-memes.comb36e4b4a-8cd8-4f56-a071-82b99f1c7922
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(22).jpgdev-memes.comeae32c18-54a8-4751-ae50-06d9acd453e9
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(23).jpgdev-memes.come7bea1c2-e3c0-4d6e-aa04-6f84f728a721
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(24).jpgdev-memes.com4622c055-215b-414b-8a6c-731723fd629e
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(25).jpgdev-memes.come34fe7a1-a8ca-423d-8e43-7549944c8c2d
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(26).jpgdev-memes.com1066108f-264a-4576-8e4f-f080a0b73ee5
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(27).jpgdev-memes.com5d74d50e-dcc7-4ada-89c4-32dad71b5dcd
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(28).jpgdev-memes.comec39af30-76b8-4741-ba59-238842190096
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(29).jpgdev-memes.comba1f0dd7-e1f2-484a-9215-d540c7f50ada
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(30).jpgdev-memes.com49634dd1-8032-4a53-bfeb-a57d5e7464c1
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(31).jpgdev-memes.comb61ffd3c-bb9b-4cdd-8192-5abdfa0d27d2
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(32).jpgdev-memes.com400ce46e-f108-43e1-92f8-6ab8dcdbf3fd
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(33).jpgdev-memes.com7d80dcbd-4a43-4922-b4d1-dc1da53ff447
https://vvgskppmennronkqbstj.supabase.co/storage/v1/object/public/memes/38e49d24-a90a-4cf9-9825-602a6c3e1bb7/dev-memes%20(34).jpgdev-memes.com0b7bdb48-97df-4eb5-bacf-83a4af9c3eaa
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
