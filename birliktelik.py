import numpy as np
from mlxtend.frequent_patterns import apriori
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

df1 = apriori(transactionMatrix, min_support=0.02, use_colnames = False, verbose=1)
#Briliktelik analizi le kurallar oluşturuldu
rules = association_rules(df1, metric = "confidence", min_threshold = 0.9)

