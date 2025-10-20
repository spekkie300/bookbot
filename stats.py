def get_word_count(string):
    return len(string.split())


def get_char_count(string):
    lowered_string = string.lower()
    char_dict = {}
    for char in lowered_string:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def sort_on(items):
    return items["num"]


def create_sorted_list(dict):
    char_list = []
    for chars in dict:
        char_list.append({"char": chars, "num": dict[chars]})

    char_list.sort(reverse=True, key=sort_on)
    return char_list
