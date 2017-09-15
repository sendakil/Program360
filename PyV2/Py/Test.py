import functools
import urllib
from bs4 import BeautifulSoup

#def fahrenheit(T):
#    return ((float(9)/5)*T + 32)
#def celsius(T):
#    return (float(5)/9)*(T-32)


#Celsius = [39.2, 36.5, 37.3, 37.8]
#f=map(lambda x: (float(9)/5)*x + 32, Celsius)
#print(list(f))

#lov=[10,20,30,40]
#reduced_value=functools.reduce(lambda x,y:x + y, lov)
#print(reduced_value)

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

page= urllib.request.urlopen(wiki)

soup = BeautifulSoup(page,'lxml')

#print(soup.prettify())

all_tables=soup.find_all("tr")
#for row in all_tables:
#    all_columns = row.find_all("td")
#    for col in all_columns:
#        print(col)



