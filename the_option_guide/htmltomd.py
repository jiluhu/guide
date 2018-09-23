def readhtml(filepath):
    import urllib
    from bs4 import BeautifulSoup
    import os
    htmlf=open(filepath,'r',encoding="utf-8")
    htmlcont=htmlf.read()
    soup = BeautifulSoup(htmlcont, "html.parser")#实例化一个BeautifulSoup对象
    [s.extract() for s in soup('script')]
    if hasattr(soup.body,"body"):
        bodyx=soup.body.body.div.div
        contentsx= bodyx.contents
        #print (contentsx)
        return contentsx
    else:
        print(soup.attrs)

def htmltomd(dir,file_name,contentsx):
    file = dir + "\\" + file_name[:-5]+".md"
    if os.path.exists(dir):
        if os.path.exists(file):
            print(file + "已存在")
            return
        else:
            realhtmltomd(file, contentsx)
            print(file + "转换成功")
    else:
        os.mkdir(dir)
        realhtmltomd(file, contentsx)
        print(file + "转换成功")

def  realhtmltomd(file,contentsx):
    if contentsx is None:
        print(file +"is none")
        return
    with open(file, 'a+') as f:
        for child in  contentsx:
            if hasattr(child, 'name'):
                if child.name=="h1":
                    #print( "==="+str(type(child))+str(child))
                    #print( child)
                    f.write("# "+str(child.string.replace('\n', '').encode("utf-8"))[2:-1]+'\n')
                elif child.name=="h2":
                    #print( child)
                    f.write('\n'+"## "+str(child.string.replace('\n', '').encode("utf-8"))[2:-1]+'\n')
                elif child.name=="h3":
                    #print( child)
                    f.write('\n'+"### "+str(child.get_text().replace('\n', '').encode("utf-8"))[2:-1]+'\n')
                elif child.name=="p":
                    #print( child)
                    f.write(str(child.get_text().replace('\n', '').encode("utf-8"))[2:-1]+'\n')
            #<div class="next">Next: <a href="call-option.aspx">Call Option <img border="0" src="images/arrow.gif"/></a></div>
                elif child.name=="div":
                    if "class" in child.attrs:
                        if str(child["class"])=="[\'next\']":
                            #title = child.get_text()
                            #print(child.get_text())
                            f.write(str(child.get_text().replace('\n', '').encode("utf-8"))[2:-1]+'\n')


import os.path
rootdir = 'content'
list_dir = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
for i in range(0, len(list_dir)):
    path = os.path.join(rootdir, list_dir[i])
    if os.path.isfile(path):
        dirs = list_dir[i][:-4]
        print("====目录 " + dirs+" ==================================")
        list_dir2 = os.listdir(dirs.strip())
        print(len(list_dir2))
        for i in range(0, len(list_dir2)):
            dirs2 =list_dir2[i]
            #print(dirs2)
            path2 = os.path.join(dirs,dirs2)
            if os.path.isfile(path2):
                filename = list_dir2[i]
                print("=======文件 " + filename +" ===path:"+path2)
                contentsx=readhtml(path2)
                htmltomd(dirs+"_1",filename,contentsx)