# YoutubePlaylistScraper

This is a simple script that scraps the data of videos from given playlist.

Data is saved into .JSON file, so it allows you to work with that.

This small project is based mostly on a pytube library.

### How to run it:
```
> git pull https://github.com/midnight1337/YoutubePlaylistScraper.git

> pip install -r requirements.txt

> python main.py
```

#### Example usage:
```
> python main.py

Please provide an YT public playlist URL: https://www.youtube.com/playlist?list=PL0PoKNuzUC_sWCvwmI5TXoflXJdzJeiAl
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