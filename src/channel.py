import json
import os
from googleapiclient.discovery import build

api_key: str = os.environ.get('API_KEY_Y')

youtube = build('youtube', 'v3', developerKey="AIzaSyDtqM8u8P5KZGagcXMXtYLb9WUtuF-z9-I")


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
