import datetime

from src.channel import YouTubeMixin
import isodate


class PlayList(YouTubeMixin):
    """
    Класс, который инициализируется id плейлиста
    и имеет следующие публичные атрибуты:
    название плейлиста, ссылку на плейлист.
    """

    def __init__(self, playlist_id: str):
        self.__total_duration = None
        self.__playlist_id = playlist_id
        self.__url = f"https://www.youtube.com/playlist?list={playlist_id}"
        self.__playlist = self.get_service().playlistItems().list(playlistId=self.__playlist_id, part='contentDetails',
                                                                  maxResults=50).execute()
        self.__video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.__playlist['items']]
        self.__video_response = self.get_service().videos().list(part='snippet,contentDetails,statistics',
                                                                 id=','.join(self.__video_ids)).execute()
        self.__channel_id = self.__video_response['items'][0]['snippet']['channelId']
        self.__playlists = self.get_service().playlists().list(channelId=self.__channel_id,
                                                               part='contentDetails,snippet', maxResults=50).execute()
        for playlist in self.__playlists['items']:
            if playlist_id == playlist['id']:
                self.__title = playlist['snippet']['title']

    @property
    def title(self):
        """Getter для title."""
        return self.__title

    @property
    def url(self):
        """Getter для url."""
        return self.__url

    @property
    def total_duration(self):
        """Getter для total_duration."""
        self.__total_duration = datetime.timedelta()
        for video in self.__video_response['items']:
            iso_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_duration)
            self.__total_duration += duration
        return self.__total_duration

    def show_best_video(self):
        """
        Возвращает ссылку на самое популярное видео
        из плейлиста (по количеству лайков).
        """
        best_video_id = ''
        max_like = 0
        for video in self.__video_response['items']:
            like_count = video['statistics']['likeCount']
            if max_like < int(like_count):
                max_like = int(like_count)
                best_video_id = video['id']
        best_video_url = f"https://youtu.be/{best_video_id}"
        return best_video_url
