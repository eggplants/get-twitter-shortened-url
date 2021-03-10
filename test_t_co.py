import os
from os.path import expanduser, isfile, join

import pytest
from dotenv import load_dotenv

import t_co

key_path = join(expanduser("~"), '.twitter.key')
if isfile(key_path):
    load_dotenv(key_path)

CK, CS, AT, AS = [os.environ.get(_)
                  for _ in ('CONSUMER_KEY', 'CONSUMER_SECRET', 'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')]
T = t_co.Shortener(CK, CS, AT, AS)


def test1():
    assert T.shorten(['google.com']) == [{'url': 'https://t.co/evEPVuy3P6',
                                          'expanded_url': 'https://google.com/', 'display_url': 'google.com', 'original_url': 'google.com'}]


def test2():
    with pytest.raises(TypeError):
        T.shorten('google.com')
