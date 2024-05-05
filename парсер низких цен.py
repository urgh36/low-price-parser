import requests
from bs4 import BeautifulSoup

url = 'https://www.ozon.ru/category/smartfony-15502/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('div', class_='product')  # предположим, что товары на странице находятся в теге <div> с классом 'product'
cheapest_product = None
cheapest_price = None

for product in products:
    price = product.find('span', class_='price').text  # предположим, что цена находится в теге <span> с классом 'price'
    # преобразуем цену в числовой формат (может потребоваться дополнительная обработка)
    price = float(price.replace('$', '').replace(',', '').strip())
    
    if cheapest_price is None or price < cheapest_price:
        cheapest_product = product
        cheapest_price = price

if cheapest_product:
    product_title = cheapest_product.find('h3').text  # предположим, что название товара находится в теге <h3>
    print(f'Самый дешевый товар: {product_title}, Цена: ${cheapest_price}')
else:
    print('Товары не найдены или страница не отформатирована ожидаемым образом.')
