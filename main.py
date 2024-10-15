import rich
from youtube_playlist_scrapper import YoutubePlaylistScrapper
from file_manager import FileManager


if __name__ == '__main__':
    playlist_url = input(
            "Please provide an YT public playlist URL: "
        )

    scrapper: YoutubePlaylistScrapper = YoutubePlaylistScrapper(
        playlist_url=[
            playlist_url
        ]
    )
    scrapper.scrap_playlist()

    FileManager.import_to_json(
        data=scrapper.playlist_data
    )

    rich.print(
        scrapper.playlist_data
    )
