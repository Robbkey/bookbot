# improting the book as a string from the stats.py
from stats import get_book_text
# improting the word_count as an int from the stats.py
from stats import word_count
from stats import count_characters 
from stats import sort_on       

# defining the main function with it's calls
def main():
    file_path = "/home/robbkey/Desktop/BootDev/github.com/Robbkey/bookbot/books/frankenstein.txt"
    # calling the function get_book_text
    book = get_book_text(file_path)
  

    # calling the function  word_count
    count = word_count(book)
  

    # calling the function count_characters
    character, list_dictionairy= count_characters(book)
  
    # sorting list of dictionairys by value key, sort_on calls function sort_on
    list_dictionairy.sort(reverse=True, key=sort_on)

    # printing a report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in range(len(list_dictionairy)):
        print(f"{list_dictionairy[i]["char"]}: {list_dictionairy[i]["value"]}")


main()
