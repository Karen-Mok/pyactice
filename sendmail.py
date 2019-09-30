#! /usr/bin/python3
# -*-coding:UTF-8-*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

sender = 'x@163.com'
pwd = 'x' #开通邮箱服务后，设置的客户端授权密码
receivers = ['x@qq.com','x@139.com']  # 接收邮件，可设置为你的邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('邮件文本内容', 'plain', 'utf-8')
message['From']=formataddr(["发信人昵称",sender])  #让收信人轻松看出邮件是谁发送的，可读性更好
message['To'] =','.join(receivers) #收信人信息(str类型)，可以与sendmail收信人个数不一致，这个只是显示在邮件的“收信人”信息中

subject = '邮件标题'
message['Subject'] = Header(subject, 'utf-8')

try:
    # 使用非本地服务器，需要建立ssl连接
    smtpObj = smtplib.SMTP_SSL("smtp.163.com", 994)
    smtpObj.login(sender, pwd)
    smtpObj.sendmail(sender, receivers, message.as_string()) 
    #receiver为列表，决定谁真正收到邮件
    print ("邮件发送成功")
    smtpObj
except smtplib.SMTPException as e:
    print ("Error: 无法发送邮件.Case:%s" % e)
