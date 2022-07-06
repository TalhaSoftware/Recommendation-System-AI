# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 17:57:22 2021

@author: TalhaSoftware
"""

import numpy as np
from apyori import apriori
import pandas as pd
from mlxtend.frequent_patterns import association_rules

#veriler dosyasını matris haline dönüştürür
def readFile(fname):
    fread = open(fname,"r")
    fread.readline()  #Bilgi satırını atlamak icin yapılmıştır.
    data = []
    for row in fread:
        templine = []
        row = row.replace("\n","")
        data.append(row.split())

    return data
    
def extractUniqueItemAndBuyer(data):
    # Tüm oyunları bir listeye ekler
    item_list =  []
    buyer_list = []
    for elem in data:
        item_list.append(elem[3])
        buyer_list.append(elem[0])
    unique_item_list = list(set(item_list)) #Kac farklı oyun oldugunu bulur
    unique_buyer_list = list(set(buyer_list)) #Kac farklı alıcı oldugunu bulur
    unique_buyer_list.sort() #Sıralama yapıldı
    return unique_buyer_list,unique_item_list


#İlişki matrisini oluşturur
def generateTransactionMatrix(data,unique_buyer_list,unique_item_list):
    n_of_buyer = len(unique_buyer_list)
    n_of_item = len(unique_item_list)
    transactionMatrix = pd.DataFrame(0,index=np.arange(n_of_buyer),columns=unique_item_list)

    
    for elem in data:
        buyer = elem[0]
        item = elem[3]
        buyerInd = unique_buyer_list.index(buyer)
        transactionMatrix.iloc[buyerInd,transactionMatrix.columns.get_loc(item)] = 1
    return transactionMatrix
    

data = readFile("veriler.txt")
unique_buyer_list,unique_item_list = extractUniqueItemAndBuyer(data)
transactionMatrix = generateTransactionMatrix(data,unique_buyer_list,unique_item_list)


#Bu alttaki kodlar her bir kullanıcın aldığı oyunları listeye aktarmak için yazılmıştır
j = 0
bl = []
while(j<1001):
    l = []
    z=0
    for i in transactionMatrix.iloc[j]:
        if(i == 1):
            l.append(transactionMatrix.columns[z])
        z+=1
    bl.append(l)
    j+=1

new_list=[x for x in bl if len(x)>=2]

"""
df = pd.DataFrame(new_list)
liste = df.to_numpy()
liste = liste.tolist()


for i in liste:
    s=0
    for j in i:
        if(j==None):
            i[s] = "nan"
        s+=1
"""        

#Burada apriori algoritmasına verdik Tavsiye Sistemi için
kurallar = apriori(new_list,min_support=0.02,min_confidence=0.2,min_lift=3,min_length=2)

conclusion = list(kurallar)

# print(conclusion)#Obje olarak döndüğü için Listeye çevirdik

# import json

# result = json.dumps(conclusion)

# print("**********************************\n")
# print(result)



def bastir(x):
    elemanlar = []
    for i in x:
        # print(i)
        elemanlar.append(i)
    
    dosya = open("onerilenler.txt","a+")
    for i in elemanlar:
        dosya.write(i.replace("İ","I")+" ")
    dosya.write("\n")
    dosya.close()

for i in range(0,len(conclusion)):
    try:
        bastir(conclusion[i][0])
        # print("****************")
    except:
        pass





