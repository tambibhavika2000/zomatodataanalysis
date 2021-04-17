import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS

zomato_data = pd.read_csv(r"myapp/zomato.csv", encoding='latin-1') 
zomato_india=zomato_data.loc[zomato_data['Country Code'] == 1] 
zomato_india.drop('Country Code',axis='columns', inplace=True)
zomato_india.drop('Locality Verbose',axis='columns', inplace=True)
zomato_india.drop('Currency',axis='columns', inplace=True)

def getwordcloud(city):
    city_data = zomato_india.groupby('City').get_group(city) 
    competitor_restaurants = set()
    popular=list(city_data['Cuisines'].value_counts().sort_values(ascending = False).index)
    for restaurant, cuisine in zip(city_data['Restaurant Name'], city_data['Cuisines']):
        if(cuisine in popular):
            competitor_restaurants.add(restaurant)

    competitor_data = pd.DataFrame(None)
    for col in competitor_restaurants:
        d = city_data[city_data['Restaurant Name'] == col]
        competitor_data = pd.concat((competitor_data, d), axis=0)

    stopwords = set(STOPWORDS)
    wordcloud = (WordCloud(width = 1440, height = 1080, relative_scaling = 1, stopwords = stopwords).generate_from_frequencies(competitor_data['Restaurant Name'].value_counts()))
    fig = plt.figure(1, figsize=(20,10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("static/"+city+"wordcloud.svg")