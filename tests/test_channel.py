import pytest
from src.channel import Channel


@pytest.fixture
def moscowpython():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


def test_channel_init(moscowpython):
    assert moscowpython.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'


def test_print_info():
    channel = Channel('1')
    assert channel.print_info() is None
