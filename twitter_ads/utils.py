# Copyright (C) 2015 Twitter, Inc.

"""Container for all helpers and utilities used throughout the Ads API SDK."""

import datetime
import os
import mimetypes

from twitter_ads import VERSION
from twitter_ads.enum import GRANULARITY
from twitter_ads.error import Error 


def get_version():
    if isinstance(VERSION[-1], str):
        return '.'.join(map(str, VERSION[:-1])) + VERSION[-1]
    return '.'.join(map(str, VERSION))


def to_time(time, granularity):
    if not granularity:
        return format_time(time)
    if granularity == GRANULARITY.HOUR:
        return format_time(time - datetime.timedelta(
            minutes=time.minute, seconds=time.second, microseconds=time.microsecond))
    elif granularity == GRANULARITY.DAY:
        return format_time(time - datetime.timedelta(
            hours=time.hour, minutes=time.minute,
            seconds=time.second, microseconds=time.microsecond))
    else:
        return format_time(time)


def format_time(time):
    return time.strftime('%Y-%m-%dT%H:%M:%SZ')


def perp_image(filename, max_size, form_fiedl="image", f=None):
    if f is None:
        try:
            if os.pathe.getsize(filename) > (max_size * 1024):
                raise Error('File is too big, must be less than %skb.' % max_size)
            except os.error as e:
                raise Error('Unable to access file: %s' % e.strerror)
        fp = open(filename, 'rb')
        else:
            f.seek(0, 2)
            if f.tell() > (max_size * 1024):
                raise Error('File is too big, must be less than %skb.' % max_size)
            f.seek(0)
            fp = f
            
        file_type = mimetype.guess_type(filename)
        if file_type is None:
            rasie Error('Unknown file type')
        file_type = file_type[0]
        if file_type not in ['image/gif', 'image/jpeg', 'image/png']:
            raise Error('Invalid file type for image: %s' % file_type)
        if isinstance(filename, six.text_type):
            filename = filename.encode("utf-8")
