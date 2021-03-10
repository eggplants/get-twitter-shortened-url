from urllib.parse import urlparse

import tweepy
from url_normalize import url_normalize


class URLError(Exception):
    pass


class Shortener:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.tweepy_api = self._auth()

    def _auth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        return api

    def _url_to_idn(self, url):
        url_p = urlparse(url)
        if url_p.scheme == '':
            url_p._replace(scheme='http')
        elif url_p.scheme not in ('http', 'https'):
            raise URLError('invalid scheme: {}'.format(url_p.scheme))

        return url_normalize(url_p.geturl())

    def shorten(self, url):
        urls = []
        urls.extend(url)
        normalized_urls = [self._url_to_idn(_) for _ in urls]
        link_text = '\n'.join(normalized_urls)
        own_id = self.tweepy_api.me().id
        sent_dm = self.tweepy_api.send_direct_message(own_id, text=link_text)
        self.tweepy_api.destroy_direct_message(sent_dm.id)
        message_dict = sent_dm.message_create['message_data']['entities']['urls']
        for idx in range(len(message_dict)):
            message_dict[idx].pop('indices')
            message_dict[idx]['original_url'] = urls[idx]

        return message_dict
