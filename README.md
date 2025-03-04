YoutubePlaylistScraper
===

This simple tool allows you to quickly scrap the metadata of any playlist on youtube.

* _Playlist_: title, owner, total views, count of videos
* _Video:_ title, time duration, total views, url

Fetched data is saved into .JSON file.

---

In order to start scraping a playlist, simply provide an playlist url that has public access.

You can also provide few URLs at once, just separate them by using comma.

---

### How to run it:
```
> git clone https://github.com/midnight1337/YoutubePlaylistScraper.git

> uv sync

> uv run main.py
```

---

### Example usage with given output:

- Single playlist example:

```
> python main.py

Please provide an YT public playlist URL: https://www.youtube.com/playlist?list=PL0PoKNuzUC_sWCvwmI5TXoflXJdzJeiAl
```

```
Processing 5/5 videos from: 𝕡𝕠𝕤𝕥 𝕡𝕦𝕟𝕜. Progress: |████████████████████████████████████████| 100.00%
{
    0: {
        'title': '𝕡𝕠𝕤𝕥 𝕡𝕦𝕟𝕜',
        'owner': 'midnight ;]',
        'length': 5,
        'views': 0,
        'url': 'https://www.youtube.com/playlist?list=PL0PoKNuzUC_sWCvwmI5TXoflXJdzJeiAl',
        'videos': {
            0: {
                'title': 'She Past Away - Rituel',
                'duration': '4:56',
                'views': '6 512 155',
                'url': 'https://www.youtube.com/watch?v=H5Kkw-Puhho'
            },
            1: {
                'title': 'looking over your city at 3am (Post-Punk playlist)',
                'duration': '31:52',
                'views': '2 509 921',
                'url': 'https://www.youtube.com/watch?v=mk_TkG-NCI4'
            },
            2: {
                'title': 'Underrated Songs that match the vibe of Mr. Kitty - After Dark',
                'duration': '39:15',
                'views': '462 704',
                'url': 'https://www.youtube.com/watch?v=rY8DrRLDYug'
            },
            3: {
                'title': 'The underground mix.ll (#postpunk #coldwave #synthwave)',
                'duration': '60:1',
                'views': '402 911',
                'url': 'https://www.youtube.com/watch?v=qY9mY-hyyAw'
            },
            4: {
                'title': "Alone on New Year's...(Post-punk, Bedroom pop Playlist)",
                'duration': '36:51',
                'views': '493 563',
                'url': 'https://www.youtube.com/watch?v=hgqz3WBzthg'
            }
        }
    }
}
```

Few playlists example:

```
> python main.py

Please provide an YT public playlist URL: https://www.youtube.com/playlist?list=PL0PoKNuzUC_sWCvwmI5TXoflXJdzJeiAl, https://www.youtube.com/playlist?list=PLw3A77RRI5PD9QYqiyKr3EUHk2Ac2ET83, https://www.youtube.com/playlist?list=PL8134A817825545CC
```

```
Processing 5/5 videos from: 𝕡𝕠𝕤𝕥 𝕡𝕦𝕟𝕜. Progress: |████████████████████████████████████████| 100.00%
Processing 6/6 videos from: Tash Sultana - NOTION EP. Progress: |████████████████████████████████████████| 100.00%
Processing 6/6 videos from: Alcest - Écailles De Lune Full Album. Progress: |████████████████████████████████████████| 100.00%
{
    "0": {
        "title": "𝕡𝕠𝕤𝕥 𝕡𝕦𝕟𝕜",
        "owner": "midnight ;]",
        "length": 5,
        "views": "0",
        "url": "https://www.youtube.com/playlist?list=PL0PoKNuzUC_sWCvwmI5TXoflXJdzJeiAl",
        "videos": {
            "0": {
                "title": "She Past Away - Rituel",
                "duration": "4:56",
                "views": "6 512 403",
                "url": "https://www.youtube.com/watch?v=H5Kkw-Puhho"
            },
            "1": {
                "title": "looking over your city at 3am (Post-Punk playlist)",
                "duration": "31:52",
                "views": "2 510 044",
                "url": "https://www.youtube.com/watch?v=mk_TkG-NCI4"
            },
            "2": {
                "title": "Underrated Songs that match the vibe of Mr. Kitty - After Dark",
                "duration": "39:15",
                "views": "462 715",
                "url": "https://www.youtube.com/watch?v=rY8DrRLDYug"
            },
            "3": {
                "title": "The underground mix.ll (#postpunk #coldwave #synthwave)",
                "duration": "60:1",
                "views": "402 916",
                "url": "https://www.youtube.com/watch?v=qY9mY-hyyAw"
            },
            "4": {
                "title": "Alone on New Year's...(Post-punk, Bedroom pop Playlist)",
                "duration": "36:51",
                "views": "493 577",
                "url": "https://www.youtube.com/watch?v=hgqz3WBzthg"
            }
        }
    },
    "1": {
        "title": "Tash Sultana - NOTION EP",
        "owner": "Tash Sultana",
        "length": 6,
        "views": "216 109",
        "url": "https://www.youtube.com/playlist?list=PLw3A77RRI5PD9QYqiyKr3EUHk2Ac2ET83",
        "videos": {
            "0": {
                "title": "Tash Sultana - Synergy (Official Audio)",
                "duration": "4:19",
                "views": "1 898 328",
                "url": "https://www.youtube.com/watch?v=7C_niY2Ku_A"
            },
            "1": {
                "title": "Gemini",
                "duration": "5:33",
                "views": "1 277 861",
                "url": "https://www.youtube.com/watch?v=1GUyZSxRuak"
            },
            "2": {
                "title": "Notion",
                "duration": "5:41",
                "views": "6 988 993",
                "url": "https://www.youtube.com/watch?v=dbAuwBvOGNU"
            },
            "3": {
                "title": "Jungle",
                "duration": "5:16",
                "views": "19 933 834",
                "url": "https://www.youtube.com/watch?v=CZvP7PwUAwM"
            },
            "4": {
                "title": "Big Smoke, Pt. 1 (Live)",
                "duration": "11:13",
                "views": "477 727",
                "url": "https://www.youtube.com/watch?v=Okh4qzkU-iA"
            },
            "5": {
                "title": "Big Smoke, Pt. 2 (Live)",
                "duration": "9:38",
                "views": "2 787 169",
                "url": "https://www.youtube.com/watch?v=yAgcNiFlCcI"
            }
        }
    },
    "2": {
        "title": "Alcest - Écailles De Lune Full Album",
        "owner": "jaffeyannai",
        "length": 6,
        "views": "278 490",
        "url": "https://www.youtube.com/playlist?list=PL8134A817825545CC",
        "videos": {
            "0": {
                "title": "Écailles de lune (Part II)",
                "duration": "9:52",
                "views": "873 262",
                "url": "https://www.youtube.com/watch?v=gk_gIOSHviA"
            },
            "1": {
                "title": "Ecailles de lune, Pt. 2",
                "duration": "9:48",
                "views": "540 313",
                "url": "https://www.youtube.com/watch?v=GhRNN8BIZxE"
            },
            "2": {
                "title": "Percées de lumière",
                "duration": "6:38",
                "views": "1 042 362",
                "url": "https://www.youtube.com/watch?v=e-kW-rxzJ_0"
            },
            "3": {
                "title": "Alcest - Abysses",
                "duration": "1:41",
                "views": "82 654",
                "url": "https://www.youtube.com/watch?v=Ggnq40Oj_eI"
            },
            "4": {
                "title": "Solar Song",
                "duration": "5:25",
                "views": "181 297",
                "url": "https://www.youtube.com/watch?v=46W_462hdPo"
            },
            "5": {
                "title": "Alcest - Sur L'Océan Couleur De Fer",
                "duration": "8:18",
                "views": "1 661 131",
                "url": "https://www.youtube.com/watch?v=waGDKnFv_Vg"
            }
        }
    }
}
```