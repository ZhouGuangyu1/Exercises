#-*- coding:utf-8 -*-
from PIL import ImageTk
from tkinter import *
import requests
import os
import time
import re
import urllib
import time
import tkinter.font as tkFont
import pygame
if not os.path.exists('./songs'):
   os.mkdir('./songs')




# 初始化声音0.5,第一首歌,透明度
Transparency = 1
i = 0
v = 0.5
def music():
   try:
      class Downloader():
         def __init__(self):
             self.headers = {
                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
                         }
             self.search_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.top&searchid=34725291680541638&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w={}&g_tk=5381&jsonpCallback=MusicJsonCallback703296236531272&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
             self.fcg_url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback9239412173137234&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback9239412173137234&uin=0&songmid={}&filename={}.m4a&guid=8208467632'
             self.downloader_url = 'http://dl.stream.qqmusic.qq.com/{}.m4a?vkey={}&guid=8208467632&uin=0&fromtag=66'
         def run(self, keyword, num=1):
             # Step1
             # 根据歌名搜索，获取所需的信息
             print('正在搜索中...')
             res = requests.get(self.search_url.format(keyword), headers=self.headers).text
             # media_mid
             media_mid_temp = re.findall('"media_mid":"(.*?)"', res)
             media_mid = []
             for i in range(len(media_mid_temp)):
                 media_mid.append('C400'+media_mid_temp[i])
             # songmid
             songmid = re.findall('"lyric_hilight":".*?","mid":"(.*?)","mv"', res)
             # singer
             singer_temp = re.findall('"singer":\[.*?\]', res)
             singer = []
             for s in singer_temp:
                 singer.append(re.findall('"name":"(.*?)"', s)[0])
             # songname
             songname = re.findall('},"name":"(.*?)","newStatus"', res)
             # Step2
             # 获取下载地址
             print('获取资源中，请等待几秒...')
             urls = []
             del_idex = []
             songname_keep = []
             singer_keep = []
             for m in range(len(media_mid)):
                 try:
                     fcg_res = requests.get(self.fcg_url.format(songmid[m], media_mid[m]), headers=self.headers)
                     vkey = re.findall('"vkey":"(.*?)"', fcg_res.text)[0]
                     urls.append(self.downloader_url.format(media_mid[m], vkey))
                     songname_keep.append(songname[m])
                     singer_keep.append(singer[m])
                 except:
                     print('[Warning]:One song lost...')
                 time.sleep(0.5)
             # Step3
             # 下载歌曲
             print('准备下载...')
             if num > len(urls):
                 print('[Warning]:Only find %d songs...' % len(urls))
                 num = len(urls)

             for n in range(num):
                 print('正在下载 第%d 首歌...' % (n+1))

                 filepath = './songs/{}'.format(songname_keep[n].replace("\\", "").replace("/", "").replace(" ", "")+'_'+singer_keep[n].replace("\\", "").replace("/", "").replace(" ", "")+'.m4a')
                 urllib.request.urlretrieve(urls[n], filepath)
                 scale = 25
                 n = chr(9608)
                 for i in range(scale+1):
                    a = n*i
                    b = " "*(scale-i)
                    c = (i/scale)*100
                    print("\r{:^3.0f}%{}{}".format(c,a,b),end="")
                    time.sleep(0.1)
             print('完成下载到桌面,放置在本目录songs文件中')


      if __name__ == '__main__':

         titles = '【曲库来自QQ音乐】'
         print("{:-^30}".format(titles))

         keyword = ("%s" % e1.get())
         songnum = ("%s" % e2.get())
         if keyword and songnum != "":
            try:
               if int(songnum) > 0:

                  songnum = int(songnum)


                  dl = Downloader()
                  dl.run(keyword, songnum)
               else:
                  print("你输入的数量不正确，请重新输入")
            except:
               print("你输入的数量不正确，请重新输入")



         else:
            print("你输入的信息不全，请重新输入")



   except:
      print("抱歉，无法下载，可能是QQ音乐无版权")


# 暂停

def pause():
   global go
   go = 0

   pygame.mixer.music.pause()



# 取消暂停

def qxpause():

   pygame.mixer.music.unpause()


# 初始化音量




# 音量调节

def up_vol():


   global v

   v += 0.2

   pygame.mixer.music.set_volume(v)

   return v



def down_vol():

   global v


   v -= 0.2

   pygame.mixer.music.set_volume(v)

   return v

# 上一曲



def shangmusic():

   global i
   i -= 1
   if i < 0:
      i = len(song)-1


   try:

      path = r'songs\\' + song[i]

      pygame.mixer.music.load(path)
      pygame.mixer.music.play()
      return i
   except:
      print("出错")


# 下一曲

def xiamusic():
   global i
   i += 1

   if i > len(song)-1:
      i = 0





   try:

      path = r'songs\\' + song[i]

      pygame.mixer.music.load(path)
      pygame.mixer.music.play()
      return i
   except:
      print("出错")



# 文件夹路径

def addr(fp):

    for root, dirs, files in os.walk(fp):

        for fn in files:

           filelist.append(fn)

    return filelist

# 初始化音频

pygame.mixer.init()

# 初始化当前歌曲序列

pau = 'pause'

# 音乐文件夹路径
fp = r'songs\\'

# 初始化空文件列表

filelist = []

# song = ['dang.mp3','feima.wav','qingchen.mp3']


song = addr(fp)
try:

   path = fp + song[i]

   pygame.mixer.music.load(path)
except:
   print("文件夹检索有误")




# 播放音乐

def play1():
    pygame.mixer.music.play()


root = Tk()
root.attributes('-alpha', Transparency)
sw = root.winfo_screenwidth()  #得到屏幕宽度
sh = root.winfo_screenheight() #得到屏幕高度
ww = 600
wh = 360
x = (sw-ww) / 2
y = (sh-wh) / 2
root.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
ft1 = tkFont.Font(size=15,weight=tkFont.BOLD,slant=tkFont.ITALIC)
ft = tkFont.Font(size=15, weight=tkFont.BOLD,slant=tkFont.ITALIC)
ft3 = tkFont.Font(size=15, weight=tkFont.BOLD)
ft4 = tkFont.Font(size=25, weight=tkFont.BOLD)

root.title('会员歌曲下载-Zhou Guangyu')

Label(root,text="歌名：",font=ft).grid(row = 0)
Label(root,text="数量：",font=ft1).grid(row = 1)
Label(root,text="version:1.2.0",font=ft3).grid(row=0,column=2,sticky=W,padx =10,pady=5)
Label(root,text="author:Zhou Guangyu",font=ft3).grid(row=1,column=2,sticky=E,padx =10,pady=5)
Label(root,text="播放器",font=ft4).grid(row=30,column=1,sticky=W,padx =10,pady=5)



e1 = Entry(root)
e2 = Entry(root)

e1.grid(row = 0,column = 1,padx = 10,pady = 5)
e2.grid(row = 1,column = 1,padx = 10,pady = 5)


def show():
   global keyword,songnum

   music()
   e1.delete(0,END)
   e2.delete(0,END)







Button(root,text="确认下载",width=10,bg="Light Sky Blue",font="华康少女字体",command=show)\
               .grid(row=3,column=0,sticky=W,padx = 10,pady=5)


Button(root,text="退出",width=10,bg="Pale Violet Red1",font="华康少女字体",command=root.quit)\
               .grid(row=3,column=1,sticky=E,padx=10,pady=5)

Button(root,text="播放",width=10,bg="lightgreen",font="华康少女字体",command=play1)\
               .grid(row=35,column=0,sticky=W,padx=10,pady=20)
Button(root,text="暂停",width=10,bg="lightgreen",font="华康少女字体",command=pause)\
               .grid(row=35,column=1,sticky=E,padx=10,pady=20)
Button(root,text="取消暂停",width=10,bg="lightgreen",font="华康少女字体",command=qxpause)\
               .grid(row=35,column=2,sticky=W,padx=10,pady=20)
Button(root,text="增大音量",width=10,bg="lightgreen",font="华康少女字体",command=up_vol)\
               .grid(row=35,column=2,sticky=E,padx=10,pady=5)


Button(root,text="减少音量",width=10,bg="lightgreen",font="华康少女字体",command=down_vol)\
               .grid(row=37,column=2,sticky=E,padx=10,pady=5)
Button(root,text="上一曲",width=10,bg="lightgreen",font="华康少女字体",command=shangmusic)\
               .grid(row=37,column=0,sticky=W,padx=10,pady=5)
Button(root,text="下一曲",width=10,bg="lightgreen",font="华康少女字体",command=xiamusic)\
               .grid(row=37,column=1,sticky=E,padx=10,pady=5)


mainloop()
