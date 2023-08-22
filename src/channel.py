import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.environ.get('API_KEY_Y')
    youtube = build('youtube', 'v3', developerKey="AIzaSyDtqM8u8P5KZGagcXMXtYLb9WUtuF-z9-I")

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        channel_info = json.dumps(self.channel, indent=2, ensure_ascii=False)
        channel_info_dict = json.loads(channel_info)
        self.title = channel_info_dict['items'][0]['snippet']['title']
        self.description = channel_info_dict['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{channel_id}"
        self.view_count = int(channel_info_dict['items'][0]['statistics']['viewCount'])
        self.subscriber_count = int(channel_info_dict['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(channel_info_dict['items'][0]['statistics']['videoCount'])

    def __str__(self):
        """Магический метод для пользователей."""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """
        Метод срабатывает при сложении,
        складываются количества подписчиков.
        """
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """
        Метод срабатывает при вычитании,
        вычитаются количества подписчиков.
        """
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other):
        """
        Метод для сравнения "меньше"
        по количеству подписчиков.
        """
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """
        Метод для сравнения "меньше или равно"
        по количеству подписчиков.
        """
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        """
        Метод для сравнения "больше"
        по количеству подписчиков.
        """
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        """
        Метод для сравнения "больше или равно"
        по количеству подписчиков.
        """
        return self.subscriber_count >= other.subscriber_count

    @property
    def channel_id(self):
        """Getter для channel_id."""
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""
        return cls.youtube

    def print_info(self):
        """Выводит в консоль строку  с информацией о канале."""
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        channel_info = json.dumps(channel, indent=2, ensure_ascii=False)
        print(channel_info)
        return channel_info

    def to_json(self, file_to_save):
        """Сохраняет в файл значения атрибутов экземпляра Channel"""
        data = {'channel_info': []}
        data['channel_info'].append({
            'channel_id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'view_count': self.view_count,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count
        })
        with open(file_to_save, 'w') as outfile:
            json.dump(data, outfile)

        return os.path.abspath(file_to_save)
