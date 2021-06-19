from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/search?q=camera&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_2_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_2_na_na_na&as-pos=4&as-type=RECENT&suggestionId=camera&requestId=fe84f1f3-c882-4ace-9c41-3dbb68f1bbfc&as-searchtext=ca"

response = requests.get(url)
# print(response.status_code)
# print(response.content)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.a)
# print(soup.find_all)
# print(soup.find(id='next-page-link-tag'))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# for image in soup.find_all('img'):
#     print(image.get('src'))

# product = soup.find_all('div', class_='_3pLy-c row')
# print(product.string)

product = soup.find('div', attrs={'class':'_3pLy-c row'})
print(product)