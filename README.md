# get-twitter-shortened-url (`t_co`)

## `t_co` is…

- Get shortened link(s) from [Twitter URL Shortener](https://help.twitter.com/en/using-twitter/url-shortener) ([t.co](https://t.co/))
- Available on package & CLI

## Install

```bash
$ pip install get-twitter-shortened-url
```

## Usage

### from CLI

```text
$ t_co -h
usage: t_co [-h] [-k key path] [--CK consumer key] [--CS consumer key secret]
            [--AT accress token] [--AS access token secret] [-V]
            url [url ...]

Shortened link from Twitter URL Shortener(t.co)

positional arguments:
  url                   Urls you want to shorten.

optional arguments:
  -h, --help            show this help message and exit
  -k key path, --key_path key path
                        Key file path (default: ~/.twitter.key)
  --CK consumer key     Twitter consumer key.
  --CS consumer key secret
                        Twitter consumer key secret.
  --AT accress token    Twitter access token.
  --AS access token secret
                        Twitter access token secret.
  -V, --version         show program's version number and exit
```

```bash
$ cat ~/.twitter.key
CONSUMER_KEY=xxxxxxxxxxxxxxxxxxx
CONSUMER_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ACCESS_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ACCESS_TOKEN_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

$ t_co https://google.co.jp 'https://www.youtube.com/watch?v=-8OqFcLyA8o'
https://google.co.jp => https://t.co/cpMOvCJCDU
https://www.youtube.com/watch?v=-8OqFcLyA8o => https://t.co/pTZgns1Fas

$ t_co 突うずるっ.com
突うずるっ.com => https://t.co/5Z1CN94Hrb
```

### from package

```python
import t_co
CK, CS, AT, AS = '...', '...', '...', '...'
t = t_co.Converter(CK, CS, AT, AS)
t.shorten(['https://google.co.jp'])
# => [{ 'url':          'https://t.co/cpMOvCJCDU',
#       'expanded_url': 'https://google.co.jp/',
#       'display_url':  'google.co.jp',
#       'original_url': 'https://google.co.jp' }]
t.shorten(['https://google.co.jp', 'https://www.youtube.com/watch?v=-8OqFcLyA8o'])
# => [{ 'url':          'https://t.co/cpMOvCJCDU',
#       'expanded_url': 'https://google.co.jp/',
#       'display_url':  'google.co.jp',
#       'original_url': 'https://google.co.jp' },
#     { 'url':          'https://t.co/pTZgns1Fas',
#       'expanded_url': 'https://www.youtube.com/watch?v=-8OqFcLyA8o',
#       'display_url':  'youtube.com/watch?v=-8OqFc…',
#       'original_url': 'https://www.youtube.com/watch?v=-8OqFcLyA8o' }]
```

### TIPS

- Set the key using dotfile for security

```python
from os.path import expanduser, join
import os
from dotenv import load_dotenv

load_dotenv(join(expanduser("~"), '.twitter.key'))
CK, CS, AT, AS = [os.environ.get(_)
                  for _ in (
                    'CONSUMER_KEY', 'CONSUMER_SECRET',
                    'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')]
```

- Set keys on Terminal

```bash
$ export CONSUMER_KEY=xxxxxxxxxxxxxxxxxxx
$ export CONSUMER_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ export ACCESS_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ export ACCESS_TOKEN_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Development

- local test

```bash
$ act -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 --secret-file ~/.twitter.key
```

## LISENCE

MIT

## Author

eggplants (haruna)
