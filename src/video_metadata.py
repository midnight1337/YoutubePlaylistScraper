from dataclasses import asdict, dataclass, field


@dataclass(kw_only=True, frozen=True)
class VideoMetadata:
    url: str
    title: str | None = field(default=None)
    length: int | None = field(default=None)
    views: int | None = field(default=None)

    @property
    def data(self) -> dict[str, str | int | None]:
        return asdict(self)
