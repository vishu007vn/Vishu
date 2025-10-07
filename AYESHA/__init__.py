from AYESHA.core.bot import Sona
from AYESHA.core.dir import dirr
from AYESHA.core.git import git
from AYESHA.core.userbot import Userbot
from AYESHA.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Sona()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
