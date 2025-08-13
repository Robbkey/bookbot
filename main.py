# improting the book as a string from the stats.py
from stats import get_book_text
# improting the word_count as an int from the stats.py
from stats import word_count
from stats import count_characters        

# defining the main function with it's calls
def main():
    file_path = "/home/robbkey/Desktop/BootDev/github.com/Robbkey/bookbot/books/frankenstein.txt"
    # calling the function get_book_text
    book = get_book_text(file_path)
    #print(book)

    # calling the function  word_count
    count = word_count(book)
    print(f"{count} words found in the document")

    # calling the function count_characters
    character = count_characters(book)
    print(character)

main()

