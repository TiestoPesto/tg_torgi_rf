import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_ads(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
	
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		soup = BeautifulSoup(response.content, "html.parser")
		# print(soup)
		ads = soup.find_all("li", class_="cards__item")
		return ads
	else:
		raise Exception("Error getting ads from Торги-России")


def main(url):
	ads = get_ads(url)
	num = 0
	for ad in ads[:10]:
		num += 1
		title = ad.find("h3", class_="card__title").text.strip()
		description = ad.find("p", class_="card__excerpt").text.strip()
		num_lot = ad.find("b", class_="text-primary").text.strip()
		price = ad.find("p", class_="lot-cost__value")
		# image = ad.find("img", class_="item__image").get("src")
		print(f'N {num}')
		print(f"**Название:** {title}")
		print(f"**Описание** {description}")
		print(f"**Номер объявления** {num_lot}")
		print(f"**Цена:** {price}")
		print('\n\n+++++++++++++++++++++++++')
		# print(f"[Image of {title}]({image})")


if __name__ == "__main__":
	
	# URL страницы с торгами
	url = "https://торги-россии.рф/search?search=Самара&categorie_childs%5B%5D=7&categorie_childs%5B%5D=9&regions%5B%5D=63&trades-section=bankrupt&trades-type=&begin-price-from=&begin-price-to=&current-price-from=&current-price-to=&begin_bid_from=&begin_bid_to=&end_bid_from=&end_bid_to=&debtor_type=&debtor_name=&debtor_inn=&group_org=&organizer_name=&arbitr_inn="
	
	main(url)
