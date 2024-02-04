def count_words(book_text):
    return len(book_text.split())


def dictionary_builder(dict):
    letters = []
    for key, value in dict.items():
        letters.append({"letter": key, "count": value})
    return letters


def count_letters(book_text):
    letter_count = {}
    for letter in book_text:
        if letter.isalpha():
            standardized_letter = letter.lower()
            if standardized_letter in letter_count:
                letter_count[standardized_letter] += 1
            else:
                letter_count[standardized_letter] = 1

    return dictionary_builder(letter_count)


def sort_on(e):
    return e["count"]


def build_book_report(word_count, character_counts):
    start = """
--- Begin report of books/frankenstein.txt ---
{0} words found in the document
    """.format(
        word_count
    )
    end = "--- End Report ---"
    print(start)
    for character in character_counts:
        letter = character["letter"]
        count = character["count"]
        print(f"The '{letter}' character was found {count} times")
    print(end)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_counts = count_letters(text)
    letter_counts.sort(reverse=True, key=sort_on)
    print(letter_counts)
    build_book_report(word_count, letter_counts)


main()
