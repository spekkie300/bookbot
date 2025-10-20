from stats import get_word_count
from stats import get_char_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    fp = "books/frankenstein.txt"
    book_string = get_book_text(fp)
    wc = get_word_count(book_string)
    char_count = get_char_count(book_string)

    print(f"Found {wc} total words")
    print(char_count)


main()
