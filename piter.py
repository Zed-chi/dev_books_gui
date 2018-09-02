import requests
from bs4 import BeautifulSoup as web


def get_page(url):
    return requests.get(url).text


def parse_page(page, handler):
    content = web(page, "html.parser")
    return handler(content)


def books_titles(content):
    books = content.select(".products-list > div")
    return (book.a["title"] for book in books)


def print_titles(header, titles):
    print("\n{}".format(header))
    print("\n".join(titles))
    

def get_books():
    new_books_url = "https://www.piter.com/collection/new"
    soon_books_url = "https://www.piter.com/collection/soon"
    
    new_page = get_page(new_books_url)
    soon_page = get_page(soon_books_url)
    
    new_content = web(new_page, "html.parser")
    soon_content = web(soon_page, "html.parser")
    
    new_books = books_titles(new_content)
    soon_books = books_titles(soon_content)
    return {
        "new":new_books,
        "soon":soon_books,
        }


def main():
    new_books_url = "https://www.piter.com/collection/new"
    soon_books_url = "https://www.piter.com/collection/soon"
    
    new_page = get_page(new_books_url)
    soon_page = get_page(soon_books_url)
    
    new_content = web(new_page, "html.parser")
    soon_content = web(soon_page, "html.parser")
    
    new_books = books_titles(new_content)
    soon_books = books_titles(soon_content)
    
    print_titles("=== new === ", new_books)
    print_titles("=== soon ===", soon_books)
    
if __name__ == "__main__":
    main()
