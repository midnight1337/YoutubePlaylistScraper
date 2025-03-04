from dataclasses import dataclass, field

from .playlist_metadata import PlaylistMetadata
from .video_metadata import VideoMetadata


@dataclass
class PlaylistContainer:

    _container: dict[int, dict] = field(
        init=False,
        default_factory=dict
    )

    @property
    def show(self) -> dict[int, dict]:
        return self._container

    def add_playlist(self, playlist: PlaylistMetadata) -> None:
        """Add playlist metadata to the container hashmap."""
        playlist_id: int = len(
            self._container
            )
        self._container[playlist_id] = playlist.data

    def add_video_to_playlist(self, playlist_id: int, video: VideoMetadata) -> None:
        """Add video metadata to the associated playlist."""
        video_id: int = len(
            self._container[playlist_id]['videos']
            )
        self._container[playlist_id]['videos'][video_id] = video.data
