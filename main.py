#!/usr/bin/env python3

import requests
import sys


def question_to_affirmative(s):
    return s[4:-1] + '.'


url = 'http://www.czypisnaprawiljuzpolske.pl/data/data.html'

connection = requests.get(url)
connection.encoding = 'utf-8'

if not connection.ok:
    print('Coś poszło nie tak podczas łączenia się z API')
    sys.exit(1)

promises = connection.json()

not_fulfilled = [p for p in promises if p['title'] == 'Nie!']
fulfilled = [p for p in promises if p not in not_fulfilled]

if not fulfilled:
    print('PiS jeszcze nie spełnił żadnej obietnicy wyborczej.')
    sys.exit()

print('\tSpełnione obietnice wyborcze:')
for p in fulfilled:
    print(question_to_affirmative(p['description']))
