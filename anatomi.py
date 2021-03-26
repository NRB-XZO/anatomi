
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NRB SECURITY
from python_imagesearch.imagesearch import imagesearch
from pyautogui import leftClick
import pyautogui
from time import sleep
from random import randint
from os import system
from PyQt5 import QtWidgets,QtGui
from bs4 import BeautifulSoup
import requests
import sys
username = "NRB"
password = "sokaklarr"
kullanıcı_adı = pyautogui.prompt(text='Kullanıcı adınızı girin', title='NRB SECURİTY' , default='')
sifre = pyautogui.password(text='Şifrenizi giriniz.', title='NRB SECURİTY' , mask="*")
if username==kullanıcı_adı and sifre == password:
    pyautogui.alert(text='Giriş yapıldı', title='NRB SECURİTY', button="Tamam")
else:
    pyautogui.alert(text='Hatalı giriş!!', title='NRB SECURİTY', button="Tamam")
    exit()
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazı_alanı = QtWidgets.QLabel("NRB")
        self.buton = QtWidgets.QPushButton("Kopyayı başlat")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.buton.clicked.connect(self.veri_cek)
        self.show()
    def veri_cek(self):
        global sik1_liste, soru_liste, sik2_liste, sik3_liste, sik4_liste, sik5_liste
        soru = str(pyautogui.prompt(text='Soruyu yazın', title='NRB SECURİTY', default=''))
        sik1 = str(pyautogui.prompt(text='Cevap1', title='NRB SECURİTY', default=''))
        sik2 = str(pyautogui.prompt(text='Cevap2', title='NRB SECURİTY', default=''))
        sik3 = str(pyautogui.prompt(text='Cevap3', title='NRB SECURİTY', default=''))
        sik4 = str(pyautogui.prompt(text='Cevap4', title='NRB SECURİTY', default=''))
        sik5 = str(pyautogui.prompt(text='Cevap5', title='NRB SECURİTY', default=''))
        x = soru.split(" ")
        sik_1 = sik1.split(" ")
        sik_2 = sik2.split(" ")
        sik_3 = sik3.split(" ")
        sik_4 = sik4.split(" ")
        sik_5 = sik5.split(" ")
        try:
            for bvn in x:
                url = "https://teachmeanatomy.info/?s={}".format(bvn)
                responce = requests.get(url)
                html_icerigi = responce.content
                soup = BeautifulSoup(html_icerigi, "html.parser")
                for i in soup.find_all("div", {"class": "search-text"}):
                    bilgi = str(i.text)
                    soru_liste = bilgi.split((" "))

            for a1 in sik_1:
                url = "https://teachmeanatomy.info/?s={}".format(a1)
                responce = requests.get(url)
                html_icerigi = responce.content
                soup = BeautifulSoup(html_icerigi, "html.parser")
                for i in soup.find_all("div", {"class": "search-text"}):
                    bilgi_sik_1 = str(i.text)
                    sik1_liste = bilgi_sik_1.split((" "))
            for a2 in sik_2:
                url = "https://teachmeanatomy.info/?s={}".format(a2)
                responce = requests.get(url)
                html_icerigi = responce.content
                soup = BeautifulSoup(html_icerigi, "html.parser")
                for i in soup.find_all("div", {"class": "search-text"}):
                    bilgi_sik_2 = str(i.text)
                    sik2_liste = bilgi_sik_2.split((" "))
            for a3 in sik_3:
                url = "https://teachmeanatomy.info/?s={}".format(a3)
                responce = requests.get(url)
                html_icerigi = responce.content
                soup = BeautifulSoup(html_icerigi, "html.parser")
                for i in soup.find_all("div", {"class": "search-text"}):
                    bilgi_sik_3 = str(i.text)
                    sik3_liste = bilgi_sik_3.split((" "))
            for a4 in sik_4:
                url = "https://teachmeanatomy.info/?s={}".format(a4)
                responce = requests.get(url)
                html_icerigi = responce.content
                soup = BeautifulSoup(html_icerigi, "html.parser")
                for i in soup.find_all("div", {"class": "search-text"}):
                    bilgi_sik_4 = str(i.text)
                    sik4_liste = bilgi_sik_4.split((" "))
            for a5 in sik_5:
                url = "https://teachmeanatomy.info/?s={}".format(a5)
                responce = requests.get(url)
                html_icerigi = responce.content
                soup = BeautifulSoup(html_icerigi, "html.parser")
                for i in soup.find_all("div", {"class": "search-text"}):
                    bilgi_sik_5 = str(i.text)
                    sik5_liste = bilgi_sik_5.split((" "))
        except:
            pyautogui.alert(text='Aktif internet bağlantısı yok!! :(', title='NRB SECURİTY', button="Tamam")
        cevap1 = list()
        cevap2 = list()
        cevap3 = list()
        cevap4 = list()
        cevap5 = list()
        for z1 in soru_liste:
            if z1 in sik1_liste:
                cevap1.append(z1)
        for z2 in soru_liste:
            if z2 in sik2_liste:
                cevap2.append(z2)
        for z3 in soru_liste:
            if z3 in sik3_liste:
                cevap3.append(z3)
        for z4 in soru_liste:
            if z4 in sik4_liste:
                cevap4.append(z4)
        for z5 in soru_liste:
            if z5 in sik5_liste:
                cevap5.append(z5)
        end = [len(cevap1), len(cevap2), len(cevap3), len(cevap4), len(cevap5)]
        end.sort()
        try:
            if end[4] == len(cevap1):
                pyautogui.alert(text='Cevap A :)', title='NRB SECURİTY', button="Tamam")
            elif end[4] == len(cevap2):
                pyautogui.alert(text='Cevap B :)', title='NRB SECURİTY', button="Tamam")
            elif end[4] == len(cevap3):
                pyautogui.alert(text='Cevap C :)', title='NRB SECURİTY', button="Tamam")
            elif end[4] == len(cevap4):
                pyautogui.alert(text='Cevap D :)', title='NRB SECURİTY', button="Tamam")
            elif end[4] == len(cevap5):
                pyautogui.alert(text='Cevap E :)', title='NRB SECURİTY', button="Tamam")
        except:
            pyautogui.alert(text='Cevabı bulamadım :(', title='NRB SECURİTY', button="Tamam")
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
