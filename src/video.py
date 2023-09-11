from src.channel import YouTubeMixin


class Video(YouTubeMixin):
    """Класс для видео из YouTube."""

    def __init__(self, id_video: str):
        """Экземпляр инициализируется id video. Дальше все данные будут подтягиваться по API."""
        self.__id_video = id_video
        try:
            self.__video = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                            id=self.__id_video).execute()
            self.title = self.__video['items'][0]['snippet']['title']
            self.view_count = int(self.__video['items'][0]['statistics']['viewCount'])
            self.like_count = int(self.__video['items'][0]['statistics']['likeCount'])
            self.comment_count = int(self.__video['items'][0]['statistics']['commentCount'])
            self.url = f"https://www.youtube.com/channel/video/{self.__id_video}"
        except IndexError:
            self.title = None
            self.view_count = None
            self.like_count = None
            self.comment_count = None
            self.url = None

    def __str__(self):
        """Магический метод для пользователей."""
        return f"{self.title}"


class PLVideo(Video):
    """Класс для плейлиста из YouTube."""

    def __init__(self, id_video: str, id_playlist: str):
        super().__init__(id_video)
        self.id_playlist = id_playlist
