import platform
import shutil
import os
import socket

fil = open('informasjon.txt', 'w')
brukernavn = os.getlogin()
Os = platform.system()
OsVer = platform.platform()
totalt, brukt, ubrukt = shutil.disk_usage("/")
hostname = socket.gethostname()
Ip = socket.gethostbyname(hostname)

fil.write("----------Pc informasjon---------- \n")
fil.write("Brukernavnet er: " + brukernavn + "\n")
fil.write("OS: " + Os + "\n")
fil.write("OS versjon: " + OsVer + "\n \n")

fil.write("----------Diskplass informasjon---------- \n")
fil.write("Totalt: %d GB" % (totalt // (2**30)) + "\n")
fil.write("Brukt: %d GB" % (brukt // (2**30)) + "\n")
fil.write("Ubrukt: %d GB" % (ubrukt // (2**30)) + "\n \n")

fil.write("----------IP informasjon---------- \n")
fil.write("IP adressen er: " + Ip + "\n \n")
