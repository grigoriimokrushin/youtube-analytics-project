import pytest
import datetime
from src.playlist import PlayList


@pytest.fixture
def playlist():
    """Создадим фикстуру с нашим экземпляром класса PlayList."""
    return PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')


def test_init(playlist):
    """Проверим как инициализировался экземпляр."""
    assert playlist.title == "Moscow Python Meetup №81"
    assert playlist.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"
    assert str(playlist.total_duration) == "1:49:52"
    assert isinstance(playlist.total_duration, datetime.timedelta)
    assert playlist.total_duration.total_seconds() == 6592.0


def test_show_best_video(playlist):
    """Проверим метод для нахождения самого популярного видео по колличеству лайков."""
    assert playlist.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
