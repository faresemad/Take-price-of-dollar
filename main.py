#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sys import argv
from PyQt5.uic import loadUi
from requests import get
from bs4 import BeautifulSoup
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("index.ui",self)
        self.setWindowTitle("EL-Dolar By Fares Emad")    # Set A Title For My App
        self.setWindowIcon(QIcon("icon2.ico"))    # Set A Icon For My App
        self.setWindowIconText("logo")
        self.setFont(QFont("Arial Black",13)) # Set A Font For My App
        self.handelUi()
        self.saldolar()
        #==Selector Goes Here==#
#========================================================================================#
    def handelUi(self):
        self.namebank = self.findChild(QLabel , "label")
        self.leb1 = self.findChild(QLabel , "label_2")
        self.leb2 = self.findChild(QLabel , "label_3")
        self.combox = self.findChild(QComboBox , "comboBox")
        self.combox.activated.connect(self.saldolar)
        # resp=get("https://eldolar.live/").content
        # forms=BeautifulSoup(resp , "lxml")
        # listsbank=forms.findAll("h4")[2:15]
        banks=[
            "بنك عودة",
            "البنك الأهلى اليونانى بمصر"
        ]
        # for bank in listsbank:
        #     banks.append(bank.text)
        self.combox.addItem(QIcon("dolar.ico"),"بنك عودة")
        self.combox.addItem(QIcon("dolar.ico"),"البنك الأهلى اليونانى بمصر")
        # self.combox.addItems(banks)
#========================================================================================#
        #==Function Here==#
#========================================================================================#
    def saldolar(self):
        if self.combox.currentText()=="بنك عودة":
            resp1=get("https://eldolar.live/bank/AUDI/USD").text
            forms1=BeautifulSoup(resp1 , "lxml")
            x1 = forms1.findAll("p")[0].text
            x2 = forms1.findAll("p")[1].text
            self.leb1.setText(x1[16:22])
            self.leb2.setText(x2[16:21])
        elif self.combox.currentText()=="البنك الأهلى اليونانى بمصر":
            resp1=get("https://eldolar.live/bank/NBG/USD").text
            forms1=BeautifulSoup(resp1 , "lxml")
            x1 = forms1.findAll("p")[0].text
            x2 = forms1.findAll("p")[1].text
            self.leb1.setText(x1[16:22])
            self.leb2.setText(x2[16:21])
#========================================================================================#
def run():
    try:
        app=QApplication(argv)
        myapp=Mainwindow()
        myapp.show()
        app.exec_()
    except Exception as error:
        print(error)
if __name__ == "__main__":
    run()