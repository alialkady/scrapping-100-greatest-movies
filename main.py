import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

#lists
names=[]
rates=[]
grosses=[]
counter=0
#fethch the url
result = requests.get("https://www.imdb.com/list/ls055592025/")

#save page content
src = result.content

#Create soup
soup = BeautifulSoup(src,"lxml")
#get the elements you want
h3_name = soup.find_all("h3",{"class":"lister-item-header"})
rate = soup.find_all("span",{"class":"ipl-rating-star__rating"})
gross = soup.find_all("span",{"name":"nv"})


for name in h3_name:
    names.append(name.find("a").text)

for i in range(len(rate)):

    if counter%23==0:
        rates.append(rate[i].text.strip())
    counter+=1

for i in range(len(gross)):
    if(i%2!=0):
        grosses.append(gross[i].text)
print(names)
print(rates)
print(grosses)

#record data on csv file
file_lists =[names,rates,grosses]
export = zip(*file_lists)
#write the pathfolder
with open("D:\\datascience\\web scraping\\IMDB 100 greatest movie all time\\data.csv","w") as file:
    wr= csv.writer(file)
    wr.writerow(["name","rate","growth"])
    wr.writerows(export)
