import requests
from bs4 import BeautifulSoup as web


def get_page(url):
    return requests.get(url).text


def parse_page(page, handler):
    content = web(page, "html.parser")
    return handler(content)


def new_books_titles(content):
    books = content.select("#new-products")[0].ul.select("li")
    return (book.div.a["title"] for book in books)


def coming_titles(content):
    books = content.select(".book-enter")[0].ul.select("li")
    return (book.div.div.a["title"] for book in books)

    
def book_print(content):
    books = content.select(".book-print")[0].ul.select("li")
    return (book.div.div.a["title"] for book in books)


def print_titles(header, titles):
    print("\n{}".format(header))
    print("\n".join(titles))
    

def get_books():
    url = "https://dmkpress.com/"
    page = get_page(url)
    content = web(page, "html.parser")
    print_books = book_print(content)
    coming = coming_titles(content)
    return {
        "coming":coming,
        "printing":print_books,
        }


def main():
    url = "https://dmkpress.com/"
    page = get_page(url)
    content = web(page, "html.parser")
    new_books = new_books_titles(content)
    coming = coming_titles(content)
    print_books = book_print(content)
    print_titles("=== new ===", new_books)
    print_titles("=== coming === ", coming)
    print_titles("=== printed ===", print_books)
    
if __name__ == "__main__":
    main()