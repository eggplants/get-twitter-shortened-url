import os

import pytest

import t_co

CK, CS, AT, AS = [os.environ.get(_)
                  for _ in ('CONSUMER_KEY', 'CONSUMER_SECRET', 'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')]


def test1():
    assert t_co.Shortener(CK, CS, AT, AS).shorten('google.com') == [
        {'url': 'https://t.co/cpMOvCJCDU', 'expanded_url': 'https://google.co.jp/',
         'display_url':  'google.co.jp', 'original_url': 'https://google.co.jp'}]
