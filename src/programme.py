from datetime import datetime

try:
    from typing import List, Dict, Callable
except:
    pass


class Base:
    def __repr__(self):
        return str(self.__dict__)


class Channel(Base):
    def __init__(self):
        # channel Unique Id
        self.id = ''  # type: str
        # channel name
        self.name = ''
        # channel icon absolute url
        self.logo = ''
        # marks channel as pin protected
        self.is_pin_protected = False
        # if not 0 channel supports archive/catchup/replay
        self.archive_days = 0
        # channel metadata
        self.metadata = {}  # type: Dict[str, int]


class Programme(Base):
    def __init__(self):
        self.id = ''  # type: str
        # Programme Start Time in UTC
        self.start_time = None  # type: datetime or None
        # Programme End Time in UTC
        self.end_time = None  # type: datetime or None
        self.title = ''
        self.description = ''
        self.thumbnail = ''
        self.poster = ''
        self.duration = 0
        self.genres = []  # type: List[str]
        self.actors = []  # type: List[str]
        self.directors = []  # type: List[str]
        self.writers = []  # type: List[str]
        self.producers = []  # type: List[str]
        self.seasonNo = None
        self.episodeNo = None
        self.year = None  # type: int or None
        self.is_replyable = False
        # programme metadata
        self.metadata = {}  # type: Dict[str, int]