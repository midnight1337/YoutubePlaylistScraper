import json


class FileManager:

    @staticmethod
    def import_to_json(data: dict[int, dict], filename: str = "playlist.json") -> None:
        with open(file=filename, mode="w") as file:
            json.dump(
                obj=data,
                fp=file,
                indent=4,
                ensure_ascii=False
            )
