import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime


def get_data(page_number: int) -> list:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    all_books = []

    page = requests.get("https://www.amazon.ca/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_" + str(page_number) + "_books?_encoding=UTF8&pg=" + str(page_number))

    soup = BeautifulSoup(page.content, "html.parser")
    books = soup.find_all('div', attrs = { 'class': 'p13n-sc-uncoverable-faceout'})

    for book in books:

        book_array = []

        name = book.find('div', attrs = {'class': '_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y'})

        author_parent = book.find('a', attrs = {'class': 'a-size-small a-link-child'})
        if author_parent is not None:
            author = author_parent.find('div', attrs = {'class': '_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y'})
        else:
            author = None

        rating = book.find('span', attrs = {'class': 'a-icon-alt'})

        users_rated = book.find('span', attrs = {'class': 'a-size-small'})

        price = book.find('span', attrs = {'class': 'p13n-sc-price'})

        if name is not None:
            title = name.get_text()
            book_array.append(title)
        else:
            book_array.append('No Title')
        
        if author is not None:
            author = author.get_text()
            book_array.append(author)
        else:
            book_array.append('Unknown Author')
        
        if rating is not None:
            rating = rating.get_text()
            book_array.append(rating.split(" ")[0])
        else:
            book_array.append('Unknown rating')
        
        if users_rated is not None:
            users_rated = users_rated.get_text()
            book_array.append(users_rated)
        else:
            book_array.append('Unknown User Ratings')
        
        if price is not None:
            price = price.get_text()
            book_array.append(price)
        else:
            book_array.append('Unknown Price')
        
        date = datetime.date.today()
        book_array.append(date)

        all_books.append(book_array)


    return all_books


search_result = []
pages = 2

for i in range(1, pages + 1):
    data = get_data(i)
    search_result.append(data)
    pass

flatten = lambda l: [item for sublist in l for item in sublist]

search_result = flatten(search_result)

# print(search_result)
print(len(search_result))

df = pd.DataFrame(search_result, columns = ['Book_Title', 'Author', 'User_Ratings', 'Customers_Rated', 'Price', 'Date'])

df.to_csv('Amazon_Books.csv', index = False, encoding = 'utf-8')