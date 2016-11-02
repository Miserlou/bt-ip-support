import six
import requests
from random import randint
from bencode import bencode, bdecode
from .exceptions import *

__VERSION__ = '0.0.5'


def _generate_peer_id():
    """http://www.bittorrent.org/beps/bep_0020.html"""
    peer_id = '-PU' + __VERSION__.replace('.', '-') + '-'
    remaining = 20 - len(peer_id)
    numbers = [str(randint(0, 9)) for _ in range(remaining)]
    peer_id += ''.join(numbers)
    assert (len(peer_id) == 20)
    return peer_id


class HTTPTracker(object):
    """Bittorent HTTP Tracking protocol"""
    STARTED = 'started'
    STOPPED = 'stopped'
    COMPLETED = 'completed'

    def __init__(self, announce_url, timeout=2, info_hash=None, **kwds):

        self.announce_url = announce_url
        self.timeout = timeout
        self._hash = info_hash
        self.peer_id = _generate_peer_id()
        self.transaction = {}
        self.port = int(kwds.get('port', 6800))
        self.downloaded = self.uploaded = 0
        self.piece_length = int(kwds.get("piece_length", 0))
        self.ip = kwds.get('ip', None)
        self.numwant = 0
        self.events = self.STARTED
        self.interval = None

    @property
    def left(self):
        return self.piece_length - self.downloaded

    def _parse(self, response):
        """parses the response from tracker"""
        if 'failure_reason' in response:
            raise TrackerResponseException(response['failure_reason'], response)
        self.peers = response['peers']
        self.interval = response['interval']
        self.complete = response['complete']
        self.incomplete = response['incomplete']

    def get_peers(self, numwant=None):
        """get the list of peers from trackers"""
        args = {
            'info_hash': self._hash,
            'peer_id': self.peer_id,
            'port': self.port,
            'uploaded': self.uploaded,
            'downloaded': self.downloaded,
            'left': self.left,
            'ip': self.ip,
            'compact': 0
        }
        if numwant:
            args['numwant'] = numwant
        if self.events == self.STARTED:
            args['event'] = self.events
            self.events = None
        response = requests.get(self.announce_url, params=args, timeout=2.001)
        print response.content
        print response
        return bdecode(response.content)
