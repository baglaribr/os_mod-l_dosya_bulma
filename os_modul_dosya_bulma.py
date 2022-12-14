# -*- coding: utf-8 -*-

import os #modülü import etme
            
text_liste = []
for klasör_yolu, klasör_isimleri, dosya_isimler in os.walk("C:/Users"): # os modülüyle bilgisayarda dosya arama
    for i in dosya_isimler:
        if (i.endswith(".txt")): # sonu txt ile biten dosyaları bulmak
            # print("Klasör yolu: {} ---> Dosya ismi: {}".format(klasör_yolu,i))
            # print("******************************")
            text_liste.append(klasör_yolu + "--->"+i) # bulunan dosyaları listeye dahil ediyoruz

with open("txt_dosyaları.txt","w",encoding="utf-8") as file:
    for i in text_liste:
        file.write(i+"\n") # listedeki her elemanı açılan klasöre kaydediyoruz

pdf_liste = []
for klasör_yolu, klasör_isimleri, dosya_isimler in os.walk("C:/Users"):
    for i in dosya_isimler:
        if (i.endswith(".pdf")):
            # print("Klasör yolu: {} ---> Dosya ismi: {}".format(klasör_yolu,i))
            # print("******************************")
            pdf_liste.append(klasör_yolu + "--->"+i)

with open("pdf_dosyalari.txt","w",encoding="utf-8") as file:
    for i in pdf_liste:
        file.write(i+"\n")
        
mp4_liste = []
for klasör_yolu, klasör_isimleri, dosya_isimler in os.walk("C:/Users"):
    for i in dosya_isimler:
        if (i.endswith(".mp4")):
            # print("Klasör yolu: {} ---> Dosya ismi: {}".format(klasör_yolu,i))
            # print("******************************")
            mp4_liste.append(klasör_yolu + "--->"+i)

with open("mp4_dosyaları.txt","w",encoding="utf-8") as file:
    for i in mp4_liste:
        file.write(i+"\n")