from xml.etree import ElementTree as ET  # 引入解析xml文件的模块
import re
import urllib  # 引入接入网络接口API的模块

from socket import error as SocketError
import errno
import os
import string


# 调用google translator API，进行翻译
def translate(text, f, t):
    '''''模拟浏览器的行为，向Google Translate的主页发送数据，然后抓取翻译结果 '''
    # text 输入要翻译的英文句子
    text_1 = text
    # 'langpair':'en'|'zh-CN'从英语到简体中文
    values = {'hl': 'zh-CN', 'ie': 'UTF-8', 'text': text, 'langpair': "%s|%s" % (f, t)}
    # values={'hl':'zh-CN','ie':'UTF-8','text':text_1,'langpair':"'en'|'zh-CN'"}
    # values={'hl':'en','ie':'UTF-8','text':text_1,'langpair':"'zh'|'en'"}
    url = 'http://translate.google.cn'  # 这个地址至关重要，写错了没有输出。网上好多 url = 'http://translate.google.cn/translate_t'，行不通
    data = urllib.urlencode(values)
    req = urllib.Request(url, data)
    # 模拟一个浏览器
    browser = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)'
    req.add_header('User-Agent', browser)
    # 向谷歌翻译发送请求
    response = urllib.urlopen(req)
    # 读取返回页面
    html = response.read()
    # print(html)
    # 从返回页面中过滤出翻译后的文本
    # 使用正则表达式匹配
    # 翻译后的文本是'TRANSLATED_TEXT='等号后面的内容
    # .*? non-greedy or minimal fashion
    # (?<=...)Matches if the current position in the string is preceded
    # by a match for ... that ends at the current position
    p = re.compile(r"(?<=TRANSLATED_TEXT=).*?;")
    m = p.search(html)
    # print m
    text_2 = m.group(0).strip(';')
    return text_2


translate("你好", 'en','zh-CN')