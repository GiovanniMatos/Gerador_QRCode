#pip install pyqrcode
import pyqrcode
import png
import os

print("""\033[36m
##########################
    Gerador de QRcode
##########################\033[0;0m
\033[31mby: kira0666@protonmail.com\033[0;0m
""")
nome = input("Nome do QRcode: ")
link_qrcode = input("Digite a url: ")
qrcode = pyqrcode.create(link_qrcode)
qrcode.png(nome+'.png', scale=8)

print("QRcode gerado com sucesso!")
os.system("ls")