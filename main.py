from stats import get_word_count
from stats import get_char_count
from stats import create_sorted_list


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    fp = "books/frankenstein.txt"
    book_string = get_book_text(fp)
    wc = get_word_count(book_string)
    char_count = get_char_count(book_string)
    sorted_list = create_sorted_list(char_count)

    print(f"Found {wc} total words")
    print(sorted_list)


main()
