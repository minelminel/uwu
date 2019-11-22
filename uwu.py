#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: michael lawrenson
@date:   11/20/19
@git:    https://github.com/minelminel/uwu.git
@remarks:
    $ sudo mv ./uwu /usr/local/bin/uwu && chmod +x /usr/local/bin/uwu
    $ uwu
    ✧･ﾟ: *✧･ﾟ♡*(ᵘʷᵘ)*♡･ﾟ✧*:･ﾟ✧ echo "this is a regular bash shell, mostly"
    ✧･ﾟ: *✧･ﾟ♡*(ᵘʷᵘ)*♡･ﾟ✧*:･ﾟ✧ echo "preface strings with /uwu/ to translate"
    ✧･ﾟ: *✧･ﾟ♡*(ᵘʷᵘ)*♡･ﾟ✧*:･ﾟ✧ echo "use CTRL+C to quit, or type /exit/"
"""
import os, re, sys, requests
from colorama import init as colorama_init
from termcolor import colored

def init():
    colorama_init()

init()
senpai_says = "<<nuzzles>>"
sad_emoji = ".·´¯`(>▂<)´¯`·."
happy_emoji = "✧･ﾟ: *✧･ﾟ♡*(ᵘʷᵘ)*♡･ﾟ✧*:･ﾟ✧"
prompt = " "
_PS1 = happy_emoji + prompt
PS1 = colored(_PS1, 'magenta')

def translate(phrase):
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    params = dict(text=phrase,lang="en-ja",format="plain",
    key="trnsl.1.1.20191121T060546Z.33f6299fef4bb603.df7991a5ef0ef0f8021497db03f51b475b819cd1")
    try:
        r = requests.post(url, params=params)
        output = r.json().get('text').pop()
    except:
        output = sad_emoji
    return output

def parse_input(cmd):
    if cmd=='exit':
        sys.exit()
    elif cmd.startswith('uwu'):
        phrase = cmd.replace('uwu','').strip()
        output = translate(phrase) if phrase else sad_emoji
        print(output)
    elif re.search('notice me senpai', cmd):
        print(senpai_says)
    else:
        os.system(cmd)

def main_loop(_func, _input):
    try:
        while True:
            _func(input(_input))
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(str(e))
        sys.exit(1)

if __name__ == '__main__':
    main_loop(_func=parse_input, _input=PS1)
