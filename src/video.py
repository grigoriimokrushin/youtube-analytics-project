from src.channel import Channel


class Video(Channel):
    """Класс для видео из YouTube."""

    def __init__(self, id_video: str):
        """Экземпляр инициализируется id video. Дальше все данные будут подтягиваться по API."""
        self.__id_video = id_video
        self.video = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                id=self.__id_video).execute()
        self.title = self.video['items'][0]['snippet']['title']
        self.view_count = int(self.video['items'][0]['statistics']['viewCount'])
        self.like_count = int(self.video['items'][0]['statistics']['likeCount'])
        self.comment_count = int(self.video['items'][0]['statistics']['commentCount'])
        self.url = f"https://www.youtube.com/channel/video/{self.__id_video}"

    def __str__(self):
        """Магический метод для пользователей."""
        return f"{self.title}"


class PLVideo(Video):
    """Класс для плейлиста из YouTube."""
    def __init__(self, id_video: str, id_playlist: str):
        super().__init__(id_video)
        self.id_playlist = id_playlist


