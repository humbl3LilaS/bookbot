import sys

from stats import get_word_count, get_word_occurrence, get_sort_words


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    content = get_book_text(path)
    num_words = get_word_count(content)
    occurrence_dic = get_word_occurrence(content)
    sorted_words = get_sort_words(occurrence_dic)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    for word in sorted_words:
        curr_char = word["character"]
        if curr_char.isalpha():
            print(f"{curr_char}: {word["count"]}")


main()
