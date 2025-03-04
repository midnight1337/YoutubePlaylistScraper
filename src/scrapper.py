import pytube
import rich

from .playlist_metadata import PlaylistMetadata
from .playlists_container import PlaylistContainer
from .progress_bar import ProgressBar
from .video_metadata import VideoMetadata


class Scrapper:

    def __init__(self, playlists: list[str]) -> None:
        self._playlist_container: PlaylistContainer = PlaylistContainer()
        self._progress_bar: ProgressBar = ProgressBar()
        self._playlists: list[str] = playlists

    @property
    def playlist_container(self) -> dict[int, dict]:
        return self._playlist_container.show

    def scrap(self) -> None:
        rich.print(
            f"\nPlaylists collected: {len(self._playlists)}\n"
        )

        self._scrap_playlist_metadata()
        self._scrap_videos_metadata()

    def _scrap_playlist_metadata(self) -> None:
        """Scrap playlist metadata."""

        for url in self._playlists:
            playlist = pytube.Playlist(
                url=url
            )

            # playlist with 0 views raises an ValueError which is raised in a pytube library
            try:
                playlist_views: int = playlist.views
            except ValueError:
                playlist_views: int = 0

            self._playlist_container.add_playlist(
                playlist=PlaylistMetadata(
                    title=playlist.title,
                    owner=playlist.owner,
                    length=playlist.length,
                    views=playlist_views,
                    url=url
                )
            )

    def _scrap_videos_metadata(self) -> None:
        """Scrap all videos metadata from playlists."""
        fails: list = []

        for playlist_id, playlist_data in self._playlist_container.show.items():
            playlist = pytube.Playlist(
                url=playlist_data['url']
            )

            for url in playlist:
                # For some reason scraping a YouTube video randomly raises an exception so retry loop is needed.
                retry_count: int = 0
                max_count: int = 3
                while retry_count < max_count:
                    try:
                        video = pytube.YouTube(
                            url=url
                        )
                        video_metadata: VideoMetadata = VideoMetadata(
                            title=video.title,
                            length=video.length,
                            views=video.views,
                            url=url
                        )

                        self._playlist_container.add_video_to_playlist(
                            playlist_id=playlist_id,
                            video=video_metadata
                        )
                    except pytube.exceptions.PytubeError as e:
                        retry_count += 1

                        if retry_count == max_count:
                            fails.append(f"Failed to fetch a data from video {url=}. {e}")

                            video_metadata: VideoMetadata = VideoMetadata(
                                url=url
                            )

                            self._playlist_container.add_video_to_playlist(
                                playlist_id=playlist_id,
                                video=video_metadata
                                )
                            break
                        continue
                    else:
                        self._progress_bar.progress_bar(
                            progress=0,
                            total=playlist_data['length'],
                            playlist_title=playlist_data['title']
                        )
                        break

        # for fail in fails:
        #     rich.print(fail)

    @classmethod
    def convert_video_duration_in_seconds_into_minutes(cls, total_seconds: int) -> str:
        minutes, seconds = divmod(total_seconds, 60)
        duration: str = f"{minutes}:{seconds}"
        return duration

    @classmethod
    def _nicely_format_any_number(cls, number: int) -> str:
        return f"{number:,}".replace(",", " ")
