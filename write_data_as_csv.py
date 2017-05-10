#!/usr/bin/env python
# coding=utf-8

"""write tabular data as csv file/string.

"""

from __future__ import print_function, unicode_literals

import csv
import sys

import six


def main():
    rows = [
        ("2017-05-10", "order1", 30, True, False, '{"foo": "bar"}'),
        ("2017-05-10", "order2", 30, True, False, '{"abc": "def"}'),
        ("2017-05-10", "order2", 30, True, False, '{"ghi": "xyz"}'),
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
    if six.PY2:
        with open("/tmp/t1.out", "wb") as f:
            w = csv.writer(f)
            w.writerows(rows)
    else:
        with open("/tmp/t1.out", "w", newline="") as f:
            w = csv.writer(f)
            w.writerows(rows)


if __name__ == '__main__':
    main()
