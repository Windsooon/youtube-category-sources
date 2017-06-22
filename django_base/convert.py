import requests
from collections import namedtuple


class PlayList:

    def __init__(
            self, playlist_id=None, user_id=None,
            user_name=None, max_results=20):

        self.base_url = 'https://www.googleapis.com/youtube/v3/'
        self.user_name = user_name
        self.max_results = max_results
        if playlist_id and not user_id:
            self.playlist_id = playlist_id
        else:
            self.channel_id = self.userid_to_channalid(user_id)
        self.key = 'AIzaSyBABK-dxkscLAibISE0-cgNW9Wk7wd5uEY'
        self.playlist_info = self.base_url + 'playlists?part=snippet&id=' + \
            self.playlist_id + '&key=' + self.key

    @staticmethod
    def object_hook(d):
        return namedtuple('X', d.keys())(*d.values())

    def userid_to_channalid(self, user_id):
        url = self.base_url + 'channels?key=' + self.key + \
            'forUsername=' + self.user_name + '&part=id'
        return self.requests_api(url)['items'][0]['id']

    def requests_api(self, url, format='json'):
        if format == 'json':
            return requests.get(url).json()
        else:
            return requests.get(url)

    def get_playlist_info(self):
        playlist_json = self.requests_api(self.playlist_info)
        playlist = self.object_hook(playlist_json)
        self.channel_id = playlist.items[0]['snippet']['channelId']
        datas = {
            'inner': 5,
            'real_id': playlist.items[0]['id'],
            'channel_id': playlist.items[0]['snippet']['channelId'],
            'channel_title': playlist.items[0]['snippet']['channelTitle'],
            'name': playlist.items[0]['snippet']['localized']['title'],
            'description': (
                playlist.items[0]['snippet']
                ['localized']['description']
            ),
            'thumbnails': (
                playlist.items[0]['snippet']
                ['thumbnails']['default']['url']
                .rsplit('/', 1)[0]),
            'last_update_time': self.get_video_info()
        }
        return datas

    def get_video_info(self):
        self.video_info = self.base_url + \
            'search?part=snippet&type=video&order=date&' + 'maxResults=' + \
            str(self.max_results) + '&playlistId=' + self.playlist_id + \
            '&channelId=' + self.channel_id + '&key=' + self.key
        video_json = self.requests_api(self.video_info)
        video = self.object_hook(video_json)
        return video.items[0]['snippet']['publishedAt']

    def add_playlist(self, datas):
        headers = {'Content-type': 'application/json'}
        local_url = 'http://127.0.0.1/api/playlist/'
        r = requests.post(url=local_url, json=datas, headers=headers)
        return r.text

first = PlayList('PLzH6n4zXuckpXGbML1y7pHxCkMRYYoG-c')
d = first.get_playlist_info()
first.add_playlist(d)
