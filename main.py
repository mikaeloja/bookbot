import sys
from stats import get_word_count, get_char_stats, get_sorted_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = get_word_count(book_text)
    char_counts = get_char_stats(book_text)
    sorted_chars = get_sorted_chars(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
        else:
            continue
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

main()
