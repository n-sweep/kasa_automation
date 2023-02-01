#!/usr/bin/env python3
# smart light/crontab automation

import os
from sys import argv


def import_routine(module_name, name='routine'):
    try:
        module = __import__(module_name, globals(), locals(), [name])
    except ImportError:
        return None

    return vars(module)[name]


def main():
    module = argv[1]
    routine = import_routine(f"routines.{module}")

    routine()


if __name__ == "__main__":
    main()
