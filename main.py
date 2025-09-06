from stats import *
import sys
# Reads the content of a book file and returns it as a string
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    #Error handeling
    if len(sys.argv)!= 2:
        sys.exit("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    # Read the book text
    arg = f"{sys.argv[1]}"
    book_text = get_book_text(arg)
    # Count the words
    num_words = get_num_words(book_text)
    # Print the result
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {arg}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    # Prints a dictionary of all chars and number of occurences
    print("--------- Character Count -------")
    print_sorted_list(dic_sort_list(get_char_count(book_text)))
    print("============= END ===============")
main()