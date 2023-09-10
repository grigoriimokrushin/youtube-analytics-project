import pytest
from src.video import Video, PLVideo


@pytest.fixture
def gil_in_python():
    """Создадим фикстуру с нашим экземпляром класса Video."""
    return Video('AWX4JnAnjBE')


@pytest.fixture
def pl_meetup78():
    """Создадим фикстуру c экземпляром класса PLVideo."""
    return PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')


def test_video_init(gil_in_python):
    """Проверим как экземпляр класса Video инициализировалcя."""
    assert gil_in_python.title == 'GIL в Python: зачем он нужен и как с этим жить'
    assert gil_in_python.like_count == 2265


def test_playlist_init(pl_meetup78):
    """Проверим как экземпляр класса PLVideo инициализировалcя."""
    assert pl_meetup78.title == 'MoscowPython Meetup 78 - вступление'
    assert pl_meetup78.like_count == 9


def test_video_str(gil_in_python):
    """Проверяем наш магический метод класса Video."""
    assert str(gil_in_python) == 'GIL в Python: зачем он нужен и как с этим жить'


def test_playlist_str(pl_meetup78):
    """Проверяем наш магический метод класса PLVideo."""
    assert str(pl_meetup78) == 'MoscowPython Meetup 78 - вступление'
