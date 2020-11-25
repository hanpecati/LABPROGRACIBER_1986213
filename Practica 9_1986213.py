import smtplib

smtpObject = smtplib.SMTP('smtp.gmail.com', 587)
smtpObject.starttls()

fromsome = str(input("Cuenta: "))
passw = input("Password: ")
smtpObject.login(fromsome,passw)

tosome = str(input("Para: "))
subj = str(input("asunto: "))
msgbody = str(input("Mensaje: "))


smtpObject.sendmail(fromsome,tosome,msgbody)
smtpObject.quit()

     