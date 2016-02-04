#!/usr/bin/env python3

import requests
import sys


def question_to_affirmative(s):
    return s[4:-1] + '.'


def get_promises():
    url = 'http://www.czypisnaprawiljuzpolske.pl/data/data.html'

    connection = requests.get(url)
    connection.encoding = 'utf-8'

    if not connection.ok:
        raise ValueError('Coś poszło nie tak podczas łączenia się z API.')

    return connection.json()


def get_not_fulfilled(promises=None):
    if promises is None:
        promises = get_promises()
    return [p for p in promises if p['title'] == 'Nie!']


def get_fulfilled(promises=None):
    if promises is None:
        promises = get_promises()
    return [p for p in promises if p['title'] != 'Nie!']


def main():
    fulfilled = get_fulfilled()

    if not fulfilled:
        print('PiS jeszcze nie spełnił żadnej obietnicy wyborczej.')
        sys.exit()

    print('\tSpełnione obietnice wyborcze:')
    for p in fulfilled:
        print(question_to_affirmative(p['description']))


if __name__ == '__main__':
    main()
