# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 17:28:45 2021

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
    


data = readFile("veriler.txt")

t = []
df = pd.DataFrame(data)

# eskij = "1000"
# for i in data:
#     for j in i:
#         eskij = j
#         while(j==eskij):
            

# kurallar = apriori(transactionMatrix,min_support=0.02,min_confidence=0.2,min_lift=3,min_length=2)

# print(list(kurallar))

