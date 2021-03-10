#!/usr/bin/env python
import argparse
import http.client as httplib
import os
import sys
from os.path import expanduser, isfile, join

from dotenv import load_dotenv
from t_co import __version__
from t_co.shortener import Shortener


class HttpConnectionNotFountError(Exception):
    pass


def check_connectivity(url="www.google.com", timeout=3):
    conn = httplib.HTTPConnection(url, timeout=timeout)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except Exception as e:
        print(e, file=sys.stderr)
        return False


def parse_args(test=None):
    """Parse arguments."""

    parser = argparse.ArgumentParser(
        prog='t_co',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Shortened link from Twitter URL Shortener(t.co)')

    parser.add_argument('url', metavar='url', nargs='+', type=str,
                        help='Urls you want to shorten.')
    parser.add_argument('-k', '--key_path', metavar='key path', type=str,
                        help='Key file path (default: ~/.twitter.key)',
                        default=join(expanduser("~"), '.twitter.key'))
    parser.add_argument('--CK', metavar='consumer key', type=str,
                        help='Twitter consumer key.')
    parser.add_argument('--CS', metavar='consumer key secret', type=str,
                        help='Twitter consumer key secret.')
    parser.add_argument('--AT', metavar='accress token', type=str,
                        help='Twitter access token.')
    parser.add_argument('--AS', metavar='access token secret', type=str,
                        help='Twitter access token secret.')

    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s {}'.format(__version__))

    if test:
        return parser.parse_args(test)
    else:
        return parser.parse_args()


def get_keys(args):
    ck, cs, at, as_ = '', '', '', ''
    if isfile(args.key_path):  # check envfile
        load_dotenv(args.key_path)

    arg_keys = [args.CK, args.CS, args.AT, args.AS]
    env_names = set(os.environ)
    key_names = (
        'CONSUMER_KEY', 'CONSUMER_SECRET',
        'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')
    key_names_set = set(key_names)

    for k, v in zip(key_names, arg_keys):  # check argkeys
        if v:
            os.environ[k] = v

    if key_names_set & env_names == key_names_set:  # check envvars
        ck, cs, at, as_ = [os.environ.get(_) for _ in key_names]

    return (ck, cs, at, as_)


def main():
    if not check_connectivity():
        raise HttpConnectionNotFountError
    args = parse_args()
    keys = get_keys(args)
    res_dicts = Shortener(*keys).shorten(args.url)
    for res_dict in res_dicts:
        print('{} => {}'.format(res_dict['original_url'], res_dict['url']))


if __name__ == '__main__':
    main()
