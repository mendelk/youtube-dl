# https://www.chabad.org/therebbe/livingtorah/player_cdo/aid/1900564/jewish/A-Symbiotic-People.htm
# https://www.chabad.org/multimedia/media_cdo/aid/3963304/jewish/Do-You-Believe-in-Water.htm

# coding: utf-8
from __future__ import unicode_literals

import re

from .common import InfoExtractor

class ChabadOrgIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?chabad\.org/[a-z_/]+/aid/(?P<id>[0-9]+)/[0-9a-zA-Z/]+'
    _TEST = {
        'url': 'https://www.chabad.org/multimedia/media_cdo/aid/3963304/jewish/Do-You-Believe-in-Water.htm',
        'md5': '83b947c4cc4c7e8f03d5f5939d060d99',
        'info_dict': {
            'id': '3963304',
            'ext': 'mp4',
            'title': 'Do You Believe in Water?',
            'thumbnail': r're:^https?://.*\.jpg$',
            # TODO more properties, either as:
            # * A value
            # * MD5 checksum; start the string with md5:
            # * A regular expression; start the string with re:
            # * Any Python type (for example int or float)
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        media_content = self._download_webpage('https://www.chabad.org/multimedia/mediaplayer/flash_media_player_content.xml.asp?what=json&aid={0}'.format(video_id), video_id)
        iid = re.search(r'\"Id\":\s\"([0-9]+)\"', media_content).group(1)

        # TODO more code goes here, for example ...
        title = self._og_search_title(webpage)

        return {
            'id': video_id,
            'title': title,
            'url': 'http://www.chabad.org/multimedia/mediaplayer/flash_media_player_content.xml.asp?what=load&aid={0}&iid={1}&mtype=mp4'.format(video_id, iid),
            'ext': 'mp4',
            'thumbnail': self._og_search_thumbnail(webpage)
            # TODO more properties (see youtube_dl/extractor/common.py)
        }
