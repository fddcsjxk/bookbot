def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = word_count(text)
    num_chars = char_count(text)
    sorted = dict_sorted(num_chars)
    print("report comin' through...")
    print(f"{num_words} words counted in {book_path}")
    for item in sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']} is in it {item['num']} times.")
    print("...yeah, that about does it.")

def sort_by(d):
    return d["char"]

def dict_sorted(num_chars):
    sorted_list = []
    for ch in num_chars:
        sorted_list.append({"char": ch, "num": num_chars[ch]})
    sorted_list.sort(reverse=False, key=sort_by)
    return sorted_list


def char_count(text):
    lower_text = text.lower()
    letter_counts = {}
    for char in lower_text:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return letter_counts

def word_count(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()
main()