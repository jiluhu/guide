import requests
from translator.HandleJs import Py4Js


def translate(tk, content):
    if len(content) > 4891:
        print("翻译的长度超过限制！！！")
        return
    param = {'tk': tk, 'q': content}
    try:
        import socket
        timeout = 20
        socket.setdefaulttimeout(timeout)

        result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=en
        &tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
        &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""", params=param,timeout = 500)

    # 返回的结果为Json，解析为一个嵌套列表
    #for text in result.json():
    #    print(text)
        return result.json()
    except UnicodeDecodeError as e:
        print('-----UnicodeDecodeError url:',e)
    except socket.timeout as e:
        print("-----socket timout:", e)

def getHtml(url):
    import socket
    import time
    try:
        timeout =20
        socket.setdefaulttimeout(timeout)# 这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置  
        sleep_download_time=10
        time.sleep(sleep_download_time)# 这里时间自己设定  
        request=urllib.request.urlopen(url)  # 这里是要读取内容的url  
        html=request.read()  # 读取，一般会在这里报异常  
        request.close()  # 记得要关闭 
        return html
    except UnicodeDecodeError as e:
        print('-----UnicodeDecodeError url:', url)
    except socket.timeout as e:
        print("-----socket timout:", url)

def main():
    js = Py4Js()

    content1 = """Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to do it.
        Although that way may not be obvious at first unless you're Dutch.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let's do more of those!"""

    #content="hello world"
    content=""" Bear Put Spread
The bear put spread option trading strategy is employed when the options trader thinks that the price of the underlying asset will go down moderately in the near term.
Bear put spreads can be implemented by buying a higher striking in-the-money put option and selling a lower striking out-of-the-money put option of the same underlying security with the same expiration date.
By shorting the out-of-the-money put, the options trader reduces the cost of establishing the bearish position but    forgoes the chance of making a large profit in the event that the underlying asset    price plummets. The bear put spread options strategy is also know as the bear put debit spread as a debit is taken    upon entering the trade.
"""
    tk = js.getTk(content)
    translate(tk, content)


if __name__ == "__main__":
    main()
