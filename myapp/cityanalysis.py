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

def getcitydata(city):
    city_data = zomato_india.groupby('City').get_group(city) 
    plt.figure(figsize=(11,7))
    plt.bar(city_data['Locality'].value_counts().sort_values(ascending = False).index, city_data['Locality'].value_counts().sort_values(ascending = False),color=(0.2, 0.4, 0.6, 0.6),edgecolor='blue')
    plt.xlabel( city + 'Localities')
    plt.ylabel('Count')
    plt.xticks(rotation = -90)
    maxi=max(city_data['Locality'].value_counts().sort_values(ascending = False))
    plt.yticks(np.arange(0,maxi, maxi//4))
    plt.title('Distribution of Restaurants in '+ city)
    plt.savefig("static/"+city+".svg")


def getcuisine(city):
    city_data = zomato_india.groupby('City').get_group(city) 
    plt.figure(figsize=(11,7))
    plt.barh(city_data['Cuisines'].value_counts().sort_values(ascending = False).index, city_data['Cuisines'].value_counts().sort_values(ascending = False),color=(1, 0.1, 0.6, 0.6),edgecolor='red')
    plt.ylabel("Cuisines")
    plt.title('Visualising Popularity of various cuisines in '+ city)
    plt.savefig("static/"+city+"cuisine.svg")


def competitor(city):
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

    mean_competitor_data = competitor_data.groupby('Restaurant Name').mean()[['Average Cost for two', 'Price range', 'Aggregate rating', 'Votes']]
    mean_competitor_data.hist(figsize=(12,9))
    plt.savefig("static/"+city+"comparision.svg")

