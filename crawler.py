# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import os
# import re
import traceback
import urllib
import time


class AppURLopener(urllib.FancyURLopener):
    version = "'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'"


urllib._urlopener = AppURLopener()


# 创建文件夹
def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)

# 解析页面
def analyse_url(ele):
    html = urllib.urlopen(ele).read()
    soup = BeautifulSoup(html, 'lxml')  # 实例化一个对象;括号内后者为解析网页方式，当然可以用自带的html.parser，不过偶尔会有坑=="
    return soup

# # 递归下载
# def r_dl(url,filename):
#     try:
#         urllib.urlretrieve(url,filename)
#     except urllib.ContentTooShortError:
#         print "Retrieval incomplete. Network's not good. Reloading..."
#         r_dl(url,filename)


# reg = re.compile('_s.jpg$')  # 取消则获取原始尺寸的图_1
box = ['1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13']

for gpNum in box:
    # gpNum = raw_input(u'输入要下载分类的序号: ')  # 只有1,2,3,5,6,7,8,9,10,11,12,13,莫名缺少4. 嗯,这样也是麻烦.直接扔循环里算了.
    url = 'http://caizhi.shejiben.com/more_material-h%s' % gpNum
    pNum = analyse_url(url).select('p.page_num a:nth-of-type(11)')[0].get_text()  # 先解析第1页并返回soup实例;bs4不支持:nth-last-    child();好在页面上的分页元素数目是固定的,所以就这么粗暴地拿每个分类的总页数了

    urlList = [url]  # 先实例化一个list,后续的子页链接还得扔到里头

    for pn in range(2, int(pNum) + 1):
        urlList.append('http://caizhi.shejiben.com/more_material-%sp%s' % (gpNum, pn))

    sn = 1  # 图片编号,因有重名,加此以区分而免于覆盖

    imgChunkCountOmega = len(analyse_url(urlList[-1]).select('div.cz_img_content > span'))
    imgChunkCountAlpha = len(analyse_url(urlList[0]).select('div.cz_img_content > span'))
    imgChunkCountTotal = imgChunkCountOmega + imgChunkCountAlpha * (len(urlList) - 1)  # 计算每个分组的图片总数

    for sp in urlList:
        analyse_url(sp)  # 开始从头逐一解析list中所有的url

        imgChunk = analyse_url(sp).select('div.cz_img_content > span')  # 该分组下所有的span的list
        imgGpName = analyse_url(sp).select('div.cz_r_title')[0].get_text()  # 该分组之名

        dirPath = u'D:\\Exercises\\%s\\' % imgGpName  # 没最后的俩反斜杠,下的图片只会和这文件夹同级
        create_folder(dirPath)

        for i in imgChunk:
            try:
                imgUrl = i.img['src']
                # imgUrl = reg.sub('.jpg', imgUrl)  # 取消则获取原始尺寸的图_2
                imgName = str(sn) + '_' + i.img['alt']
                # print i.prettify()  # 单独每个span元素,它包含了a与img
                # print imgUrl, imgName
                # r_dl(imgUrl, dirPath + '%s.jpg' % imgName)  # 咱的问题倒不是与它相关
                urllib.urlretrieve(imgUrl, dirPath + '%s.jpg' % imgName)
                print str(sn) + u' of %s DL OK' % imgGpName
                if sn == imgChunkCountTotal:
                    print u'<%s> ダウンロードが完了しました' % imgGpName
                sn += 1
            except Exception, e:
                traceback.print_exc()
                time.sleep(20)
