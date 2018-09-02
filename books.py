from dmkpress import get_books as dmk_books
from piter import get_books as pit_books
from bhv import get_books as bhv_books
from williams import get_books as wil_books
"""
from nit import get_new_books as nit_books
from infra import get_new_books as infr_books
from technosphere import get_new_books as tech_books
"""


def print_titles(distr, books):
    for header, titles in books.items():
        print("\n=== {}: {} ===".format(distr, header))
        print("-", "\n- ".join(titles))


def main():
    print_titles("DMKpress", dmk_books())
    print_titles("Piter press", pit_books())
    print_titles("BHV press", bhv_books())
    print_titles("Williams press", wil_books())


if __name__ == "__main__":
    main()
