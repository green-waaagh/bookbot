from stats import *
import sys

try:
    book_addres = sys.argv[1]
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_addres}...")
    print("----------- Word Count ----------")
    num_words=get_num_words(book_addres)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    dict=get_num_characters(book_addres)
    letters_list=sort_list(book_addres)
    for i in letters_list:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()
