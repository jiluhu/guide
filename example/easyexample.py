import urllib.request


def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html


def saveHtml(file_name, file_content):
    #    注意windows文件命名的禁用符，比如 /
    with open(file_name.replace('/', '_') + ".html", "wb") as f:
        #   写文件用bytes而不是str，所以要转码
        f.write(file_content)


#aurl = "http://www.view.sdu.edu.cn/info/1003/75240.htm"
aurl = "http://www.theoptionsguide.com/"
html = getHtml(aurl)
saveHtml("index", html)

print("下载成功")

