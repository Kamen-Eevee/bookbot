def count_words(file):
    words = file.split()
    return(len(words))

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def character_count(file):
    characters = {}
    lower_case_file = file.lower()
    for i in lower_case_file:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return(characters)

def sort_char(dict):
    return dict["num"]

def character_report(book_path, word_count, char_dict):
    list_of_chars = []
    for key in char_dict:
        if key.isalpha():
            list_of_chars.append({"key" : key, "num" : char_dict[key]})
    list_of_chars.sort(reverse = True, key = sort_char)
    get_report(book_path, word_count, list_of_chars)

def get_report(book_name, word_count, char_list):
    print (f"Start of report on", book_name)
    print (f"The book contains", word_count, "words.")
    for i in range(0, len(char_list)):
        print(f"The letter", char_list[i]["key"], "appears in the book", char_list[i]["num"], "times.")
    print ("END OF REPORT")
def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = count_words(file_contents)
    char_count = character_count(file_contents)
    character_report(book_path, word_count, char_count)
    

main()