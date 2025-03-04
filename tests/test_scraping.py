from src import Scrapper
import pytest


class TestScrapper:

    @pytest.fixture()
    def scrapper(self) -> Scrapper:
        return Scrapper(
            playlists=[
                'https://www.youtube.com/playlist?list=PL0PoKNuzUC_sWCvwmI5TXoflXJdzJeiAl'
            ]
        )

    def test_scraping(self, scrapper: Scrapper):
        assert not scrapper.playlist_container
