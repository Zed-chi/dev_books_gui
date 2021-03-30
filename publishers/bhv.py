import requests
from bs4 import BeautifulSoup as web


def get_page(url):
    response = requests.get(url)
    response.encoding = "cp1251"
    return response.text


def parse_page(page, handler):
    content = web(page, "html.parser")
    return handler(content)


def books_titles(content):
    books = content.select(".bookInfo")
    return [book.a.get_text() for book in books]


def print_titles(header, titles):
    print("\n{}".format(header))
    print("-", "\n- ".join(titles))


def get_books():
    new_books_url = "http://www.bhv.ru/books/new.php"
    new_page = get_page(new_books_url)
    new_content = web(new_page, "html.parser")
    new_books = books_titles(new_content)[:15]
    return {
        "new": new_books,
    }


def main():
    new_books_url = "http://www.bhv.ru/books/new.php"
    new_page = get_page(new_books_url)
    new_content = web(new_page, "html.parser")
    new_books = books_titles(new_content)
    print_titles("=== new === ", new_books)


if __name__ == "__main__":
    main()
