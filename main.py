##################### Extra Hard Starting Project ######################
import datetime as dt
import random

import pandas

# 1. Update the birthdays.csv
data=pandas.read_csv("birthdays.csv")
bir_day_list=data.day.to_list()
bir_mon_list=data.month.to_list()

final_birthday=[]
for i in range(len(bir_mon_list)):
    a=str(bir_day_list[i])
    a=a.replace(".0","")
    b = str(bir_mon_list[i])
    # print(a)
    if len(a)==1:
        a="0"+a
    if len(b)==1:
        b="0"+b

    final_birthday.append(b+"-"+a)
# print(final_birthday)
# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
mon = str(now.month)
date = str(now.day)
if len(date) == 1:
    date = "0" + date
if len(mon) == 1:
    mon = "0" + mon
# print(month)
final_date = mon + "-" + date
# print(final_date)
row=data[(data.day==now.day) & (data.month==now.month)]
bir_name=(row.name.item())
bir_email=(row.email.item())
# print(bir_email)

isDate = False
if final_date in final_birthday:
    isDate = True
# print(isDate)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

files=["letter_1.txt","letter_2.txt","letter_3.txt"]
with open(f"letter_templates/{random.choice(files)}") as file:
    con=file.readlines()
    message =""
    for i in con:
        message=message+i
    message=message.replace("[NAME]",bir_name)



# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
connection=smtplib.SMTP("smtp.gmail.com",port=587)
connection.starttls()
connection.login(user="shreyang0605@gmail.com",password="dxlmtqvehtnnvmlq")

if isDate:
    connection.sendmail(from_addr="shreyang0605@gmail.com",to_addrs=bir_email,msg=f"Subject:Happy Birthday\n\n{message}")

connection.close()





