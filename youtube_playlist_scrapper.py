import pytube
from progress_bar import ProgressBar
import rich


class YoutubePlaylistScrapper:

    def __init__(self, playlist_url: list):
        self._playlist_url: list[str] = playlist_url
        self._playlist_data: dict = {}
        self._progress_bar: ProgressBar = ProgressBar()

    @property
    def playlist_data(self) -> dict:
        return self._playlist_data

    def scrap_playlist(self) -> None:
        self._scrap_playlist_info()
        self._scrap_videos_from_playlist()

    def _scrap_playlist_info(self) -> None:
        """Scrap playlist info."""
        for url in self._playlist_url:
            playlist = pytube.Playlist(
                url=url
            )

            playlist_id: int = len(self._playlist_data)

            # 0 views playlist raises an ValueError in Pytube lib
            try:
                views = playlist.views
            except ValueError:
                views = 0
            finally:
                playlist_views: str = self._convert_views_count_into_nice_looking_format(views=views)

            self._playlist_data[playlist_id] = {
                "title": playlist.title,
                "owner": playlist.owner,
                "length": playlist.length,
                "views": playlist_views,
                "url": playlist.playlist_url,
                "videos": {
                    id: playlist.video_urls[id] for id in range(
                        len(
                            playlist.video_urls
                        )
                    )
                }
            }

    def _scrap_videos_from_playlist(self) -> None:
        """Scrap all videos from playlist."""
        fails: list = []

        for playlist_id, playlist_data in self._playlist_data.items():
            for video_id, video_url in playlist_data['videos'].items():

                # For some reason scraping a youtube video randomly raises an exception so retry loop is needed.
                while (retry_count := 0) < 3:
                    try:
                        yt = pytube.YouTube(
                            url=video_url
                        )
                        video_title: str = yt.title
                        video_length: int = yt.length
                        video_views: int = yt.views
                    except pytube.exceptions.PytubeError:
                        retry_count += 1

                        if retry_count == 3:
                            fails.append(f"Failed to fetch a video data with {video_id=}, {video_url=}")

                            self._playlist_data[playlist_id]['videos'][video_id] = {
                                "title": None,
                                "length": None,
                                "views": None,
                                "url": video_url
                            }
                            break

                        continue
                    else:
                        video_duration: str = self.convert_video_duration_in_seconds_into_minutes(total_seconds=video_length)
                        video_views: str = self._convert_views_count_into_nice_looking_format(views=video_views)

                        self._playlist_data[playlist_id]['videos'][video_id] = {
                            "title": video_title,
                            "duration": video_duration,
                            "views": video_views,
                            "url": video_url
                        }

                        self._progress_bar.progress_bar(
                            progress=video_id + 1,
                            total=playlist_data['length'],
                            playlist_title=self._playlist_data[playlist_id]['title']
                        )
                        break

        for fail in fails:
            rich.print(fail)

    @classmethod
    def convert_video_duration_in_seconds_into_minutes(cls, total_seconds: int) -> str:
        minutes, seconds = divmod(total_seconds, 60)
        duration = f"{minutes}:{seconds}"
        return duration

    @classmethod
    def _convert_views_count_into_nice_looking_format(cls, views: int) -> str:
        return f"{views:,}".replace(",", " ")
