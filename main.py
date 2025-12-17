import sys

from stats import chars_dict_to_sorted_list, get_chars_dict, get_num_words


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)
    words_num = get_num_words(book_text)
    chars_dict = get_chars_dict(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(path_to_book, words_num, chars_sorted_list)


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_text = f.read()
    return book_text


def print_report(path_to_book, words_num, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {words_num} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()

