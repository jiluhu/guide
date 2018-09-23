import urllib.request


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
    except urllib.error.URLError as e:
        print("-----urlError url:", url)
    except socket.timeout as e:
        print("-----socket timout:", url)

def saveHtml(dir, file_name, htmlpath):
    file=dir + "\\" + file_name + ".html"
    if os.path.exists(dir):
        if os.path.exists(file):
            print(file+"已存在")
            return
        else:
            html = getHtml(htmlpath)
            if html:
             #    注意windows文件命名的禁用符，比如 /
             # with open(file_name.replace('/', '_') + ".html", "wb") as f:
                with open(file, "wb") as f:
                    #   写文件用bytes而不是str，所以要转码
                    f.write(html)
                    print(file+"下载成功")
    else:
        os.mkdir(dir)
        html = getHtml(htmlpath)
        if html:
            with open(file, "wb") as f:
                f.write(html)
                print(file+"下载成功")


def dowload(rootdir, filenames):
    filename = rootdir + '\\' + filenames
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            # print(line)
            words = line.split("  ")
            # filter('', words)
            while "" in words:
                words.remove("")
                # words.remove("\n")
            if len(words) == 1:
                print(words[0])
            elif len(words) == 2:
                name = words[1].strip("\n")
                url = words[0].strip().strip("\"")
                print(name + ":" + url)
                aurl = "http://www.theoptionsguide.com/"
                htmlpath=aurl + url
                print(htmlpath)
                saveHtml(filenames[:-4], name, htmlpath)


import os.path

rootdir = 'content'
list_dir = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
for i in range(0, len(list_dir)):
    path = os.path.join(rootdir, list_dir[i])
    if os.path.isfile(path):
        filenames = list_dir[i]
        print("====download " + filenames+"==================================")
        # os.mkdir(filename[0:-3])
        dowload(rootdir, filenames)
