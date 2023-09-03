import pytest
import json
import os
from src.channel import Channel


@pytest.fixture
def moscowpython():
    """Создадим фикстуру с нашим экземпляром класса."""
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


@pytest.fixture
def highload():
    """Создадим еще одну фикстуру с другим экземпляром класса."""
    return Channel('UCwHL6WHUarjGfUM_586me8w')


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


def test_str(moscowpython):
    """Проверяем наш магический метод."""
    assert str(moscowpython) == 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'


def test_add_and_sub(moscowpython, highload):
    """Проверяем как складываются и вычитаются наши экземпляры класса."""
    assert moscowpython + highload == 103000
    assert moscowpython - highload == -50200


def test_le_lt_ge_gt(moscowpython, highload):
    """Проверяем как сравниваются наши экземпляры класса."""
    assert (moscowpython < highload) == True
    assert (moscowpython <= highload) == True
    assert (moscowpython > highload) == False
    assert (moscowpython >= highload) == False
    assert (moscowpython == highload) == False
