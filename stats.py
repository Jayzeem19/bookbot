# Counts the number of words in the given text
def get_num_words(text):
    num_count = len(text.split())
    return num_count
# Counts the number of characters and returns a dictionary of characters with number of each occurence
def get_char_count(text):
    text_lower = text.lower()
    char_dict = {}
    for char in text_lower:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict
# Key to sort the list in the function print_sorted_list
def sort_on(chars):
    return chars["num"]
# Takes the format of a dictionary to a list of dictionaries (eg.{"char": "b", "num": 4868}) it is not sorted idk why i called
# it dic_sort_list just dont question it
def dic_sort_list(dic):
    result = []
    for char in dic:
        if char.isalpha():
            temp_dic = {}
            temp_dic["char"] = char
            temp_dic["num"] = dic[char]
            result.append(temp_dic)
    return result
#This one actually sorts it using the key from the sort_on function, then prints it
def print_sorted_list(list):
    list.sort(reverse=True, key=sort_on)
    for dic in list:
        for char in dic:
            if char != "num":
                print(f"{dic[char]}: {dic["num"]}")