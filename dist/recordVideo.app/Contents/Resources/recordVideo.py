#coding:utf-8
import cv2
import sys
import time
import smtplib
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class Recorder :

    def __init__(self) :
        self.capture = ""
        self.subject = ""
        self.filePath = ""

    # 打开摄像头
    def openCamera(self) :
        #默认打开系统内建camera 
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3,1080)
        if self.capture.isOpened() :
            print("capture init is success")
        

    # 录制视频
    def recordVideo(self) :
        # 输出的格式
        fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
        # 分辨率
        size = (1920, 1080)
        # 准备写入
        fileNameSuffix = time.strftime('%Y-%m-%d%H:%M:%S',time.localtime())
        filePath = '/Users/sober/Desktop/Record';
        outfile = cv2.VideoWriter(filePath+fileNameSuffix+'.mp4', fourcc, 20, size)
        
        futureTime = time.time() + 500
        currentTime = time.time()

        while(currentTime < futureTime) :
            currentTime = time.time();
            
            # 获取一帧 
            ret,frame = self.capture.read()

            if ret:
                #frame = cv2.flip(frame, 1)
                frame = cv2.resize(frame, size)
                outfile.write(frame)  # 写入文件
                # 将这帧转换为灰度图
                #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) == ord('q'):
                    break
            else:
                break

        self.subject = "hostName : " + socket.gethostname() + " ip: " + socket.gethostbyname(socket.gethostname());
        self.filePath = filePath + fileNameSuffix + '.mp4'
        self.capture.release()
        outfile.release()
        cv2.destroyAllWindows()

    # 发送邮件
    def sendVideoEmail(self) :
        print("begin send mail to receiver")

        mail_host="smtp.qq.com"  #设置服务器
        mail_user="11248084@qq.com"    #用户名
        mail_pass="dqqfbjdrypsvbgfh"   #口令 

        sender = '11248084@qq.com'
        receivers = ['11248084@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header("Record Video Robot", 'utf-8')
        message['To'] =  Header("Record Video Receiver", 'utf-8') 
        subject = self.subject
        message['Subject'] = Header(subject, 'utf-8')

        # 构造附件
        attachment = MIMEText(open(self.filePath,'rb').read(), 'base64', 'gb2312')
        attachment["Content-Type"] = 'application/octet-stream'
        attachment["Content-Disposition"] = 'attachment; filename=' + self.filePath
        message.attach(attachment)

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            smtpObj.quit()
            print ("send mail success")
        except smtplib.SMTPException as e:
            print ("Error: 无法发送邮件 %s",e)



recoder = Recorder()
recoder.openCamera()
recoder.recordVideo()
recoder.sendVideoEmail()