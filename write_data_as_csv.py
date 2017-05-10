#!/usr/bin/env python
# coding=utf-8

"""write tabular data as csv file/string.

"""

from __future__ import print_function, unicode_literals

import csv
import sys

import six


def _str_to_utf8(value):
    """if value is a string, convert it to utf8 bytes.

    """
    if isinstance(value, six.text_type):
        return value.encode("utf-8")
    return value


def str_to_utf8(row):
    return [_str_to_utf8(x) for x in row]


def main_py2():
    """py2 csv module doesn't supports unicode string.

    You have to encode it to utf8 before calling writerow() or writerows().

    """
    rows = [
        ("2017-05-10", "order1", 30, True, False, '{"foo": "货物"}'),
        ("2017-05-10", "订单2", 30, True, False, '{"abc": "def"}'),
        ("2017-05-10", "order3", 30, True, False, '{"ghi": "xyz"}'),
    ]

    print("=== write to stdout ===")
    w = csv.writer(sys.stdout)
    for row in rows:
        w.writerow(str_to_utf8(row))

    print("=== write to string buffer ===")
    f = six.StringIO()
    w = csv.writer(f)
    for row in rows:
        w.writerow(str_to_utf8(row))
    print(f.getvalue())

    print("=== write to real file ===")
    with open("/tmp/t1.out", "wb") as f:
        w = csv.writer(f)
        for row in rows:
            w.writerow(str_to_utf8(row))


def main_py3():
    """py3 csv module supports unicode string.

    """
    rows = [
        ("2017-05-10", "order1", 30, True, False, '{"foo": "货物"}'),
        ("2017-05-10", "订单2", 30, True, False, '{"abc": "def"}'),
        ("2017-05-10", "order3", 30, True, False, '{"ghi": "xyz"}'),
    ]

    print("=== write to stdout ===")
    w = csv.writer(sys.stdout)
    w.writerows(rows)

    print("=== write to string buffer ===")
    f = six.StringIO()
    w = csv.writer(f)
    w.writerows(rows)
    print(f.getvalue())

    print("=== write to real file ===")
    with open("/tmp/t1.out", "w", newline="") as f:
        w = csv.writer(f)
        w.writerows(rows)


if __name__ == '__main__':
    if six.PY2:
        main_py2()
    else:
        main_py3()
