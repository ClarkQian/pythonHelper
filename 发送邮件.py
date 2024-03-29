# !/usr/bin/python
# -*- coding:utf-8 -*-

import smtplib  # smtplib这个模块是管发邮件
from email.mime.text import MIMEText  # 构造邮件内容
from email.mime.multipart import MIMEMultipart  # 发带附件的邮件用的


class SendMail(object):

    def __init__(self, username, passwd, recv, title, content, file=None, email_host='smtp.163.com', port=25):
        '''
        发送邮件封装
        :param username: 发送者账号
        :param passwd: 发送者邮箱的授权码
        :param recv: 收件人
        :param title: 邮件主题
        :param content:邮件正文的内容
        :param file:附件
        :param email_host:邮箱服务器地址
        :param port:端口
        '''
        self.username = username
        self.passwd = passwd
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file
        self.email_host = email_host
        self.port = port

    def send_mail(self):
        # 发送内容的对象
        msg = MIMEMultipart()

        # 处理附件
        if self.file:
            # att = MIMEText(open(self.file).read())

            att = MIMEText(open(r'C:\Users\qq188\Desktop\deye.png', 'rb').read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="%s"' % self.file
            msg.attach(att)


        msg.attach(MIMEText(self.content))  # 邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = self.recv  # 接收者账号列表
        self.smtp = smtplib.SMTP(self.email_host, port=self.port)  # 发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
        except Exception as e:
            print('出错了。。', e)
        else:
            print('发送成功！')

    def __del__(self):
        self.smtp.quit()


if __name__ == '__main__':
    m = SendMail(
        username='xxx@xxx.com', passwd='MMMMMMMMMMMMM', recv='xxx@xx.com',
        title='发送邮件-附件', content='啊哈哈哈哈', file=r'C:\Users\qq188\Desktop\deye2.png', email_host='smtp.126.com'
    )
    m.send_mail()
