import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
#Urls
urls = ['https://prepinsta.com/accenture-interview-experience-on-campus-1/'
,'https://prepinsta.com/accenture-on-campus-interview-experience-set-2/'
,'https://prepinsta.com/accenture-interview-experience-on-campus-set-3/'
,'https://prepinsta.com/accenture-interview-experience-off-campus-through-elitmus/'
,'https://prepinsta.com/accenture-interview-experience-off-campus-through-amcat/'
,'https://prepinsta.com/accenture-interview-experience-off-campus-amcat-set-2/'
,'https://prepinsta.com/deloitte/interview-experience/set-2/'
,'https://prepinsta.com/deloitte/interview-experience/set-3/'
,'https://prepinsta.com/deloitte/interview-experience/set-4/'
,'https://prepinsta.com/capgemini-on-campus-interview-experience/'
,'https://prepinsta.com/capgemini-on-campus-interview-experience-for-freshers/'
,'https://prepinsta.com/capgemini-off-campus-interview-experience-via-cocubes/'
,'https://prepinsta.com/capgemini-off-campus-interview-experience/'
,'https://prepinsta.com/cognizant-on-campus-interview-experience/'
,'https://prepinsta.com/cts-on-campus-interview-experience-for-freshers/'
,'https://prepinsta.com/cognizant-special-package-interview-experience-and-process/'
,'https://prepinsta.com/cognizant-off-campus-drive-interview-experience/'
,'https://prepinsta.com/cts-off-campus-drive-interview-experience-through-amcat/']
flag = 0
idn = 1
for url in urls:


    r = requests.get(url)
    text = r.text
    soup = BeautifulSoup(text)

    #Fetched_the_span_Tag and Stripped the text alone
    info = [p.text.strip() for p in soup.find_all("span")]
    info_c = []

    #The Duplicate values in the List are removed
    seen = set()
    for item in info:
        if item not in seen:
            seen.add(item)
            info_c.append(item)

    #The Student Detail is separated
    stu = info_c[6:10]
    stu_n = []

    #Student is cleaned to remove ":" from the list
    #Every thing Befor ':' is removed
    for entry in stu:
        corrected = re.sub(r'.*:', '', entry)
        stu_n.append(corrected)
    #studen Data converted to tuple
    stut = tuple(stu_n)
    #Experience of the students
    exp = info_c[11:]
    exp = exp[:len(exp)-5]
    exps = '-'.join(exp)
    final = []
    #TO get the company name
    x = url.split('/')
    y = x[3].split('-')
    comp_name = y[0]
    exp_id = 'exp_'+str(idn)
    idnn=idn
    ques=[]
    qfinal = []
    #TO retieve questions from experiences
    for e in exp:
        if e.endswith('?') == True:
            ques.append(e)
    qfinal.append(exp_id)
    qfinal.append(ques)
    final.append(exp_id)
    final.append(comp_name)
    final.append(url)
    final.append(stut)
    final.append(exps)
    print(final)
    
    
    
    idn += 1
    if flag == 0:
        df = pd.DataFrame({'1' :final})
        df2 = pd.DataFrame({'1' :qfinal})
        
        flag = 1
    else:
        df[idnn] = final
        df2[idnn] = qfinal
        
df_t = df.transpose()
df2_t = df2.transpose()


print(df_t)
print(df2_t)

df_t.to_csv('list1.csv')
df2_t.to_csv('ques1.csv')

#In ques1.csv the questions are stored in lists for easier retrivel
#I couldnt find out many websites that has experience in it.

