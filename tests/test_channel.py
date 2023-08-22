import pytest
import json
import os
from src.channel import Channel


@pytest.fixture
def moscowpython():
    """Создадим фикстуру с нашим экземпляром класса."""
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


def test_channel_init(moscowpython):
    """Проверим как наш экземпляр класса инициализироваля."""
    assert moscowpython.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'
    assert moscowpython.title == 'MoscowPython'
    assert moscowpython.url == 'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A'


def test_print_info(moscowpython):
    """Проверим, что нам возвращает функция print_info."""
    channel_info = json.dumps(moscowpython.channel, indent=2, ensure_ascii=False)
    assert moscowpython.print_info() == channel_info


def test_get_service(moscowpython):
    """Проверим метод класса get_service, выдает ли он нам нужный объект."""
    assert moscowpython.get_service() == Channel.youtube

def test_to_json(moscowpython):
    """Проверит метод to_json, создал ли он фаил и правильны ли путь до него выдает."""
    assert moscowpython.to_json('python.json') == os.path.abspath('python.json')