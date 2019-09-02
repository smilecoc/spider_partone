#注意requests后有一个s,request和requests库是不一样的
import requests
from bs4 import BeautifulSoup
import bs4

#利用requestk库获取html信息
def   getHTMLtext(url):
    try:
        r = requests.get(url,timeout=30)#定义名为r的response对象，timeout约定请求时间的超时时间
        r.raise_for_status()#当请求错误时会返回错误信息，当请求成功时,即status code为200时返回None
        r.encoding=r.apparent_encoding#使本地的解析编码与网站编码一致
        return r.text
    except:
        return ""


#将html的信息放到列表中ullist
def fillunivlist(ulist,html):
    soup=BeautifulSoup(html, "html.parser")#指定BeautifulSoup的解析器为“html.parser”
    for tr in soup.find('tbody').children:#遍历获得tbody标签下的子标签，返回的是字符串类型，find只返回一个结果
        if isinstance(tr,bs4.element.Tag):# isinstance 函数用于判断两个对象的类型是否相同，判断tr是否是beautifulsoup库的tag元素，过滤掉非标签的字标签
            tds=tr('td')#找到tr标签下的所有td标签，相当于find_all
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

#格式化输出并控制输出的数量
def printunivlist(ulist,num):
    #格式化输出，^居中对齐输出,10为最大的字符串长度
    print("{:^10}\t{:^6}\t{:^10}".format("rank","univerity","province"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
        #print("suc"+str(num))

#定义主函数并赋值变量
def main():
    unifo=[]
    url="http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
    html=getHTMLtext(url)
    fillunivlist(unifo,html)
    printunivlist(unifo,20)

#运行
main()
