from stats import *

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    num_words=get_num_words("books/frankenstein.txt")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    dict=get_num_characters("books/frankenstein.txt")
    letters_list=sort_list("books/frankenstein.txt")
    for i in letters_list:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()
