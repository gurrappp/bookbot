def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dict_char = get_count_character_in_text(text)
    list_of_dict_char = convert_to_list(dict_char)
    print_report(book_path,num_words, list_of_dict_char)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_count_character_in_text(text):
    lower_string = text.lower()
    words = lower_string.split()
    my_dict = {}
    
    for word in words:
        for char in word:
            if not char.isalpha():
                continue
            if char not in my_dict:
                my_dict[char] = 1
            else:
                my_dict[char] += 1 
            
    return my_dict

def sort_on(dict):
    return dict["num"]

def convert_to_list(dictionary):
    sorted_list = []
    for ch in dictionary:
        sorted_list.append({"char":ch , "num" : dictionary[ch]})
    
    sorted_list.sort(reverse=True, key = sort_on)

    return sorted_list

def print_report(book_path, num_words, list_of_dict_char):
    print(f"--- Begin report of {book_path} ---")
    print(f"The file contains {num_words} words")
    print()
    
    for item in list_of_dict_char:
        print(f"the '{item['char']}' character was found {item['num']} times")


main()