def get_word_count(book_text):
    return len(book_text.split())

def get_char_stats(book_text):
    char_counts = {}
    for char in book_text:
        char = char.lower()
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

def get_sorted_chars(char_counts):
    dict_list = []
    for char in char_counts:
        char_dict = {
                "char": char,
                "num": char_counts[char],
        }
        dict_list.append(char_dict)
    dict_list.sort(reverse=True, key=sort_on_nums)
    return dict_list

def sort_on_nums(items):
    return items["num"]
