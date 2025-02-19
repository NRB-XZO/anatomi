#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NRB SECURITY
from python_imagesearch.imagesearch import imagesearch
from pyautogui import leftClick
import pyautogui
from time import sleep
from random import randint
from os import system
from PyQt5 import QtWidgets, QtGui
from bs4 import BeautifulSoup
import requests
import sys

username = "NRB"
password = "sokaklarr"

kullanıcı_adı = pyautogui.prompt(text='Kullanıcı adınızı girin', title='NRB SECURİTY', default='')
sifre = pyautogui.password(text='Şifrenizi giriniz.', title='NRB SECURİTY', mask="*")

if username == kullanıcı_adı and sifre == password:
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
        soru_liste, sik1_liste, sik2_liste, sik3_liste, sik4_liste, sik5_liste = [], [], [], [], [], []
        
        soru = str(pyautogui.prompt(text='Soruyu yazın', title='NRB SECURİTY', default=''))
        sik1 = str(pyautogui.prompt(text='Cevap1', title='NRB SECURİTY', default=''))
        sik2 = str(pyautogui.prompt(text='Cevap2', title='NRB SECURİTY', default=''))
        sik3 = str(pyautogui.prompt(text='Cevap3', title='NRB SECURİTY', default=''))
        sik4 = str(pyautogui.prompt(text='Cevap4', title='NRB SECURİTY', default=''))
        sik5 = str(pyautogui.prompt(text='Cevap5', title='NRB SECURİTY', default=''))
        
        try:
            for kelime in soru.split(" "):
                url = f"https://teachmeanatomy.info/?s={kelime}"
                response = requests.get(url)
                soup = BeautifulSoup(response.content, "html.parser")
                for i in soup.find_all("div", {"class": "search-text"}):
                    soru_liste.extend(i.text.split())
        
            for idx, sik in enumerate([sik1, sik2, sik3, sik4, sik5], start=1):
                liste = globals()[f"sik{idx}_liste"]
                for kelime in sik.split(" "):
                    url = f"https://teachmeanatomy.info/?s={kelime}"
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, "html.parser")
                    for i in soup.find_all("div", {"class": "search-text"}):
                        liste.extend(i.text.split())
        except requests.exceptions.RequestException:
            pyautogui.alert(text='Aktif internet bağlantısı yok!! :(', title='NRB SECURİTY', button="Tamam")
            return
        
        cevaplar = [[] for _ in range(5)]
        for i, sik_liste in enumerate([sik1_liste, sik2_liste, sik3_liste, sik4_liste, sik5_liste]):
            cevaplar[i] = [kelime for kelime in soru_liste if kelime in sik_liste]
        
        max_cevap = max(cevaplar, key=len, default=[])
        
        if max_cevap:
            harfler = ["A", "B", "C", "D", "E"]
            pyautogui.alert(text=f'Cevap {harfler[cevaplar.index(max_cevap)]} :)', title='NRB SECURİTY', button="Tamam")
        else:
            pyautogui.alert(text='Cevabı bulamadım :(', title='NRB SECURİTY', button="Tamam")

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
