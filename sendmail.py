#! /usr/bin/python3
# -*-coding:UTF-8-*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

sender = 'x@163.com'
pwd = 'x' #开通邮箱服务后，设置的客户端授权密码
receivers = ['x@qq.com','x@139.com']  # 接收邮件，可设置为你的邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEMultipart()
message['From']=formataddr(["158网易邮箱",sender])  #让收信人轻松看出邮件是谁发送的，可读性更好
message['To'] =','.join(receivers) #收信人信息(str类型)，可以与sendmail收信人个数不一致，这个只是显示在邮件的“收信人”信息中

subject = '附件发送测试'
message['Subject'] = Header(subject, 'utf-8')

#邮件正文内容
message.attach(MIMEText('附件邮件正文内容','plain','utf-8'))

#构造文本附件1
att1 = MIMEText(open("README.md").read(),"base64","utf-8")
att1["Content-Type"] = "application/octet-stream"
att1["Content-Disposition"] = 'attachment; filename="REAMME.md"'
message.attach(att1)

#构造二进制附件2
att2 = MIMEApplication(open("搞笑.mp4","rb").read()) #打开二进制文件要指定"rb"模式！
#MIMEApplication默认子类型即为"application/octet-stream"。如果想省事，可所有类型的附件都用MIMEApplication
att2.add_header("Content-Disposition","attachment",filename=("gbk","","搞笑.mp4"))  #发送中文名附件需要指定gbk编码
message.attach(att2)

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
