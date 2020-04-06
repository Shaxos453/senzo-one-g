import requests
from bs4 import BeautifulSoup

print('Hey There!')
print('This program presents the current weather for a city of your choice!')
print('Please enter the name of a city in India')
city = input().lower()
print('Now displaying the current weather for ' + city)

URL = 'https://www.wunderground.com/weather/in/'+city;
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find(class_="condition-data")
timestamp = soup.find(class_="timestamp")
datetime = timestamp.find('strong').text
temp = result.find('div', class_='current-temp').text.strip()
#tempinc = (int(temp)-32)*5/9
hitemp = result.find('span', class_= 'hi').text
#hitempinc = (int(hitemp)-32)*5/9
lotemp = result.find('span', class_= 'lo').text
#lotempinc = (int(lotemp)-32)*5/9
feelslike = result.find('div', class_='feels-like').find('span', class_= 'temp').text
#feelslikeinc = (int(feelslike)-32)*5/9

print()
print('As on: ' + datetime)
print('Current temperature = ' + temp)
print('High = ' + hitemp)
print('Low = ' + lotemp)
print('It feels like = ' + feelslike)
