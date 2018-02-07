BASE_URL = 'https://api.twitch.tv/kraken/'
BASE_HELIX_URL = 'https://api.twitch.tv/helix/'
VOD_FETCH_URL = 'https://usher.ttvnw.net/'

PERIOD_DAY = 'day'
PERIOD_WEEK = 'week'
PERIOD_MONTH = 'month'
PERIOD_ALL = 'all'
PERIODS = [PERIOD_DAY, PERIOD_WEEK, PERIOD_MONTH, PERIOD_ALL]

BROADCAST_TYPE_ARCHIVE = 'archive'
BROADCAST_TYPE_HIGHLIGHT = 'highlight'
BROADCAST_TYPE_UPLOAD = 'upload'
BROADCAST_TYPE_ARCHIVE_UPLOAD = 'archive,upload'
BROADCAST_TYPE_ARCHIVE_HIGHLIGHT = 'archive,highlight'
BROADCAST_TYPE_HIGHLIGHT_UPLOAD = 'highlight,upload'
BROADCAST_TYPE_ALL = ""

BROADCAST_TYPES = [
    BROADCAST_TYPE_ARCHIVE,
    BROADCAST_TYPE_HIGHLIGHT,
    BROADCAST_TYPE_UPLOAD,
    BROADCAST_TYPE_ARCHIVE_UPLOAD,
    BROADCAST_TYPE_ARCHIVE_HIGHLIGHT,
    BROADCAST_TYPE_HIGHLIGHT_UPLOAD,
    BROADCAST_TYPE_ALL
]

VIDEO_SORT_TIME = 'time'
VIDEO_SORT_VIEWS = 'views'
VIDEO_SORTS = [
    VIDEO_SORT_TIME,
    VIDEO_SORT_VIEWS
]

USERS_SORT_BY_CREATED_AT = 'created_at'
USERS_SORT_BY_LAST_BROADCAST = 'last_broadcast'
USERS_SORT_BY_LOGIN = 'login'
USERS_SORT_BY = [
    USERS_SORT_BY_CREATED_AT,
    USERS_SORT_BY_LAST_BROADCAST,
    USERS_SORT_BY_LOGIN
]

DIRECTION_ASC = 'asc'
DIRECTION_DESC = 'desc'
DIRECTIONS = [
    DIRECTION_ASC,
    DIRECTION_DESC
]

STREAM_TYPE_LIVE = 'live'
STREAM_TYPE_PLAYLIST = 'playlist'
STREAM_TYPE_ALL = 'all'
STREAM_TYPES = [
    STREAM_TYPE_LIVE,
    STREAM_TYPE_PLAYLIST,
    STREAM_TYPE_ALL
]

CONFIG_FILE_PATH = '~/.twitch.cfg'
