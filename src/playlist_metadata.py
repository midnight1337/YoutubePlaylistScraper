from dataclasses import asdict, dataclass, field


@dataclass(kw_only=True, frozen=True)
class PlaylistMetadata:
    title: str
    owner: str
    length: int
    views: int
    url: str
    videos: dict = field(
        init=False,
        default_factory=dict
    )

    @property
    def data(self) -> dict[str, str | int]:
        return asdict(self)
