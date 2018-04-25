
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
sender = r'hgkdzbf6@163.com'
receivers = [r'hgkdzbf6@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
mail_msg = """
<p>Python 邮件发送测试...</p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header("zbf", 'utf-8')
message['To'] =  Header("训练完啦", 'utf-8')
 
subject = '你的模型已经训练完成，别睡了去看看吧'
message['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP() 
smtp.connect('smtp.163.com',25) 
smtp.login(username, password) 
smtp.sendmail(sender, receivers, message.as_string()) 
smtp.quit()
print("邮件发送成功")
