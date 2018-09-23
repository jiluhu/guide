#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : gt1.py
# Purpose :
# Creation Date : 1390366260
# Last Modified : Wed 22 Jan 2014 06:14:11 PM CST
# Release By : Doom.zhou


import urllib.request
import sys

typ = sys.getfilesystemencoding()

def translate(querystr, to_l="zh", from_l="en"):
    '''for google tranlate by doom
    '''
    C_agent = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.165063 Safari/537.36 AppEngine-Google."}
    flag = 'class="t0">'
    tarurl = "http://translate.google.com/m?hl=%s&;sl=%s&;q=%s" % (to_l, from_l, querystr.replace(" ", " + "))
    request = urllib.request.Request(tarurl, headers=C_agent)
    page = str(urllib.request.urlopen(request).read().decode(typ))
    target = page[page.find(flag) + len(flag):]
    target = target.split("<")[0]
    return target

print(translate("Hello world"))