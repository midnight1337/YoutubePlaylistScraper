import rich

from src import FileManager, Scrapper

if __name__ == '__main__':
    prompt: str = input(
            "Please provide an YT public playlist URL: "
        )

    playlists: list[str] = prompt.split(sep=',')

    scrapper: Scrapper = Scrapper(
        playlists=playlists
    )
    scrapper.scrap()

    FileManager.import_to_json(
        data=scrapper.playlist_container
    )

    rich.print(
        scrapper.playlist_container
    )
