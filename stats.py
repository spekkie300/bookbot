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
