import sys

import colorama


class ProgressBar:

    @classmethod
    def progress_bar(cls, playlist_title: str, progress: int, total: int, length: int = 40) -> None:
        """
        Emulate a progress bar in console.

        :param playlist_title: Playlist title to display info about progress.
        :param progress: Current item.
        :param total: Total count of items.
        :param length: Length of the bar buffer.
        """
        # Calculate progress
        percent = (progress / total) * 100
        bar_length = int(length * progress / total)
        bar = '█' * bar_length + '-' * (length - bar_length)

        # Write progress on a console
        sys.stdout.write(
            colorama.Fore.YELLOW + f'\rProcessing {progress}/{total} videos from: {playlist_title}. Progress: |{bar}| {percent:.2f}%'
        )
        sys.stdout.flush()

        # Change color of the bar to green
        if progress == total:
            sys.stdout.write(
                colorama.Fore.GREEN + f'\rProcessing {progress}/{total} videos from: {playlist_title}. Progress: |{bar}| {percent:.2f}%'
            )
            sys.stdout.flush()

            # New line and reset colors
            print(colorama.Fore.RESET)
