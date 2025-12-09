from stats import get_num_words

def main():
      path_to_book = "books/frankenstein.txt"
      book_text = get_book_text(path_to_book)
      words_num = get_num_words(book_text)
      print(f"Found {words_num} total words")

def get_book_text(file_path):
        with open(file_path) as f:
            book_text = f.read()
        return book_text

main()