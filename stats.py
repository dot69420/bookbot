def get_num_words(book_text):
    words = book_text.split()
    words_num = len(words)
    return words_num


def get_chars_dict(book_text):
    chars = {}
    for char in book_text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(dict):
    return dict["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.sort(reverse=True, key=sort_on)
        return sorted_list

