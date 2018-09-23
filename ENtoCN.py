def entocn(dir, filename, sourcepath):
    import os
    targetfile = dir + "\\" + filename
    if os.path.exists(dir):
        if os.path.exists(targetfile):
            print(targetfile + "已翻译")
            return
        else:
            reamd(targetfile, sourcepath)
            print(targetfile + "翻译成功")
    else:
        os.mkdir(dir)
        reamd(targetfile, sourcepath)
        print(targetfile + "翻译成功")


def reamd(targetfile, sourcepath):
    f = open(targetfile, "w")
    for line in open(sourcepath):
        if line == "\n":
            continue
        print(line)
        print("%s" % (line), file=f)
        if line.startswith("# "):
            chinese = translator(line.replace("\n", "").replace("# ", "").strip())
            cn = '\n' + "# " + chinese[0][0][0]
            # print(cn)
            print("%s" % (cn), file=f)
        elif line.startswith("## "):
            chinese = translator(line.replace("\n", "").replace("## ", "").strip())
            cn = '\n' + "## " + chinese[0][0][0]
            # print(cn)
            print("%s" % (cn), file=f)
        elif line.startswith("### "):
            chinese = translator(line.replace("\n", "").replace("### ", "").strip())
            cn = '\n' + "### " + chinese[0][0][0]
            # print(cn)
            print("%s" % (cn), file=f)
        else:
            chinese = translator(line.replace("\n", "").strip())
            cn = chinese[0][0][0]
            # print(cn)
            print("%s" % (str(cn.encode("utf-8"))), file=f)
    f.close()


def translator(content):
    from translator.HandleJs import Py4Js
    from translator.Translator import translate
    js = Py4Js()
    # content = """ Bear Put Spread
    # The bear put spread option trading strategy is employed when the options trader thinks that the price of the underlying asset will go down moderately in the near term.
    # Bear put spreads can be implemented by buying a higher striking in-the-money put option and selling a lower striking out-of-the-money put option of the same underlying security with the same expiration date.
    # By shorting the out-of-the-money put, the options trader reduces the cost of establishing the bearish position but    forgoes the chance of making a large profit in the event that the underlying asset    price plummets. The bear put spread options strategy is also know as the bear put debit spread as a debit is taken    upon entering the trade.
    # """
    tk = js.getTk(content)
    return translate(tk, content)


def fileread(sourcedir):
    import os.path
    list_sourcedir = os.listdir(sourcedir)
    for i in range(0, len(list_sourcedir)):
        path = os.path.join(sourcedir, list_sourcedir[i])
        # if os.path.isfile(path):
        dirs = list_sourcedir[i]
        print("====目录 " + dirs + " ==================================")
        list_dir2 = os.listdir(path)
        print(len(list_dir2))
        for i in range(0, len(list_dir2)):
            dirs2 = list_dir2[i]
            # print(dirs2)
            sourcepath = os.path.join(path, dirs2)
            if os.path.isfile(sourcepath):
                filename = list_dir2[i]
                print("=======文件 " + filename + " ===path:" + sourcepath)
                entocn(dirs, filename, sourcepath)


if __name__ == '__main__':
    sourcedir = "../md/"
    fileread(sourcedir)

    # filename = "../md/Bearish Strategies_1/Bear Put Spread.md"

    # import os
    # pwd = os.getcwd()
    # filepath = os.path.join(pwd, filename)
    # reamd(filepath)
