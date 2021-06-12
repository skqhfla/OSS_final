import urllib.request
import re
import numpy as np
import os, sys, time
import datetime
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from time import sleep
import random
from urllib.request import HTTPError
from urllib.request import URLError

global res

def mailfunc(year,semester,code,c_num,mail):
    HTTPError_num = 0
    URLError_num = 0
    current_people = 0
    total_people = 0

    url = "https://hisnet.handong.edu/for_student/sugang/PLES230M.php?hak_year="+year+"&hak_term="+semester+"&hakbu=%C0%FC%C3%BC&isugbn=%C0%FC%C3%BC&injung=%C0%FC%C3%BC&eng=%C0%FC%C3%BC&prof_name=&gwamok=&gwamok_code="+code+"&ksearch=search"

    executable = sys.executable
    args = sys.argv[:]
    args.insert(0, sys.executable)

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    while(True):
        rand = random.randrange(2,8)
        sleep(rand)

        try:
            res = urllib.request.urlopen(req).read()

        except HTTPError:
            HTTPError_num = HTTPError_num + 1
            pass

        except URLError:
            URLError_num = URLError_num + 1
            pass

        soup = BeautifulSoup(res,'html.parser')
        keywords = str(soup.find_all('td', {'align': 'center'}))
        keywords = re.sub('<.+?>', '', keywords, 0).strip()
        keywords = keywords.replace(" ","")
        code2 = code+',(.*?)%,'
        keywords = re.findall(code2,keywords)

        subject = []
        for i in keywords:
            part = i.split(',')
            subject.append(part)

        row_col = list(np.shape(subject))

        for i in range(0,len(keywords)):
            if c_num == subject[i][0]:
                subject_name = subject[i][1]
                current_people = subject[i][row_col[1]-2]
                total_people = subject[i][row_col[1]-3]

        now = datetime.datetime.now()

        if int(current_people) < int(total_people):

            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.login('handong.sugang.helper@gmail.com', 'qgellbsykmrlcbdr')

            msg = MIMEText(str(subject_name)+'과목 수강신청 가능합니다')
            msg['Subject'] = (str(subject_name) +'과목 수강신청 가능합니다')
            msg['From'] = 'sugang@gmail.com'
            msg['To'] = mail

            s.sendmail('sugang@gmail.com', mail , msg.as_string())
            s.quit()

            return "%s 과목 수강신청가능합니다." %subject_name









