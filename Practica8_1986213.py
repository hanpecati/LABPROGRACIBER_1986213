import ftplib
from ftplib import FTP, FTP_PORT

#Introducir las credenciales del servidor ftp
server = input('host: ')
usr = input('user: ')
passw = input('password: ')

host = FTP(server, usr, passw)
info = host.nlst()
with open('files.txt','w+') as txt:
        for file in info:
                txt.writelines(f'{file}\n')