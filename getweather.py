
#coding: utf-8    

  
import time

import smtplib    

from email.mime.multipart import MIMEMultipart    

from email.mime.text import MIMEText    

from email.mime.image import MIMEImage 

from email.header import Header

import requests

import json

import os,re





#获取当前时间以便问候

def gettime():
    t = eval(time.strftime("%H"))
    if 0 <= t <= 11:
        words = "Good Morning"
    elif 11 < t <= 18:
        words = "Good Afternoon"
    else:
        words = "Good Night"
    return words
    







#获取天气数据模块

def get():
    try:
        global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17
        str = input("请输入你所在的城市")
        url ='http://wthrcdn.etouch.cn/weather_mini?city='+str
        response= requests.get(url)
        wearher_json=json.loads(response.text)
        a=wearher_json['data']

        a1 = ("{0:-^56}".format(gettime()))
        a2 = ("当前位置："+a['city'])
        a3 = ("温馨提示："+a['ganmao'])
        a4 = ("当前温度："+a['wendu']+'℃')
        a5 = ("--------------------------------")
        
        i = 0
        a6 = ("今天："+a["forecast"][i]['date'])
        a7 = ('风力: '+a["forecast"][i]['fengli']\
              [9:[m.start() for m in re.finditer(']', a['yesterday']['fl'])][0]])
        a8 = ('风向：'+a["forecast"][i]['fengxiang'])
        a9 = (a["forecast"][i]['high'])
        a10 = (a["forecast"][i]['low'])
        a11 = ("天气："+a["forecast"][i]['type'])
     
        i = 1
        a12 = ("明天："+a["forecast"][i]['date'])
        a13 = ('风力: '+a["forecast"][i]['fengli']\
              [9:[m.start() for m in re.finditer(']', a['yesterday']['fl'])][0]])
        a14 = ('风向：'+a["forecast"][i]['fengxiang'])
        a15 = (a["forecast"][i]['high'])
        a16 = (a["forecast"][i]['low'])
        a17 = ("天气："+a["forecast"][i]['type'])
    except:
        print("输入有误，请用中文输入国内城市名称")
        get()

    
    

#天气数据传递

get()
    

#设置smtplib所需的参数

#下面的发件人，收件人是用于邮件传输的。
def email():

    print("将通过SMTP端口发送邮件，确保您已经打开邮箱POP3/IMAP/SMTP等服务\
并获得密码")
    theme = input("请输入邮件主题：")
    def inform():
        global smtpserver,username,password,sender
        judge = input("是否用自己的邮箱发送，输入‘是’或‘否’：")
        if judge == "否":
        
            smtpserver = 'smtp.qq.com'

            username = '1786196673@qq.com'

            password = 'rkgiplpownjuecab'

            sender = '1786196673@qq.com'
        elif judge == "是":
            smtpserver = input("输入端口，例如smtp.qq.com")
            username = sender = input("请输入邮箱：")
            password = input("请输入密码（非邮箱密码）：")
        else:
            print("输入不规范，请重输：")
            inform()
    inform()
    def emailbox():
        global receiver
        receiver = input("请输入对方邮箱")
        receiver1 = ",".join(receiver)
        if "@" not in receiver1:
            print("非邮箱格式，请重输")
            emailbox()

    emailbox()
            
    #receiver='XXX@qq.com'

    #收件人可为多个收件人

    

 

    subject = theme

    #通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok

    #subject = '中文标题'

    #subject=Header(subject, 'utf-8').encode()

    

    #构造邮件对象MIMEMultipart对象

    #下面的主题，发件人，收件人，日期是显示在邮件页面上的。

    msg = MIMEMultipart('mixed') 

    msg['Subject'] = subject

    msg['From'] = "username <username>"

    #msg['To'] = 'XXX@qq.com'

    #收件人为多个收件人,通过join将列表转换为以;为间隔的字符串

    msg['To'] = receiver

    #msg['Date']='2012-3-16'

 
    #构造文字内容,按格式将天气数据打印  

    text = a1+"\n"+a2+"\n"+a3+"\n"+a4+"\n"+a5+"\n"+a6+"\n"+a7+"\n"+a8+"\n"\
       +a9+"\n"+a10+"\n"+a11+"\n"+a5+"\n"+a12+"\n"+a13+"\n"+a14+"\n"+a15\
       +"\n"+a16+"\n"+a17+"\n"+a5

    text_plain = MIMEText(text,'plain', 'utf-8')    

    msg.attach(text_plain)
       
    #发送邮件

    smtp = smtplib.SMTP()    
    
    smtp.connect(smtpserver)

    #我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。

    #smtp.set_debuglevel(1)  

    smtp.login(username, password)    

    smtp.sendmail(sender, receiver, msg.as_string())    

    smtp.quit()
    print("邮件已发送")
email()
