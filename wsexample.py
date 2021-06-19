from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/search?q=camera&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_2_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_2_na_na_na&as-pos=4&as-type=RECENT&suggestionId=camera&requestId=fe84f1f3-c882-4ace-9c41-3dbb68f1bbfc&as-searchtext=ca"

response = requests.get(url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')

titles = []
prices = []
images = []

for d in soup.find_all('div', attrs={'class':'_2kHMtA'}):
    title = d.find('div', attrs={'class':'_4rR01T'})
    # print(title.string)

    price = d.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    # print(price.string)

    image = d.find('img', attrs={'class':'_396cs4 _3exPp9'})
    # print(image.get('src'))

    titles.append(title.string)
    prices.append(price.string)
    images.append(image.get('src'))

print(titles)
print(prices)
print(images)