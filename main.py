from stats import get_word_count
from stats import get_char_count
from stats import create_sorted_list
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_string = get_book_text(file_path)
    word_count = get_word_count(book_string)
    char_count = get_char_count(book_string)
    sorted_list = create_sorted_list(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in sorted_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")


main()
