import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

zomato_data = pd.read_csv(r"myapp/zomato.csv", encoding='latin-1') 
zomato_india=zomato_data.loc[zomato_data['Country Code'] == 1] 
zomato_india.drop('Country Code',axis='columns', inplace=True)
zomato_india.drop('Locality Verbose',axis='columns', inplace=True)
zomato_india.drop('Currency',axis='columns', inplace=True)
wc=dict(zip(zomato_india['City'].value_counts().index , zomato_india['City'].value_counts()))
plt.figure(figsize = (11,7))
plt.bar(x = wc.keys(), height=wc.values())
plt.xlabel('Cities')
plt.ylabel('Number of outlets')
plt.title('No of Restaurants in different cities ')
plt.xticks(rotation = -90)
plt.savefig("static/wc.svg")