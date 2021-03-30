import requests
from bs4 import BeautifulSoup as web


def get_page(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    return response.text


def parse_page(page, handler):
    content = web(page, "html.parser")
    return handler(content)


def books_titles(content):    
    books = content.select(".node-promoted header h2 a")
    return [book.get_text() for book in books]


def print_titles(header, titles):
    print("\n{}".format(header))
    print("-", "\n- ".join(titles))


def get_books():
    new_books_url = "https://nostarch.com/"
    new_page = get_page(new_books_url)
    new_content = web(new_page, "html.parser")
    new_books = books_titles(new_content)
    return {
        "new": new_books,
    }


def main():
    new_books_url = "http://www.williamspublishing.com/indexns.shtml"
    new_page = get_page(new_books_url)
    new_content = web(new_page, "html.parser")
    new_books = books_titles(new_content)
    print_titles("=== new === ", new_books)


if __name__ == "__main__":
    main()
