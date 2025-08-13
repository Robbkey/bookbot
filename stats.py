def get_book_text(file_path):
    # opening the book under the given path
    with open(file_path) as f:
        # copying the string containt in the book to a variable
        file_contents = f.read()
        return file_contents

def word_count(file_contents):
    words = file_contents.split()
    word_counts = len(words)
    return word_counts

def count_characters(file_contents):
    # making it so all characters in the book are lower case ones
    book = file_contents.lower()
    # transforming a string of words into a list of characters
    character = list(book)
    dic = {}
    # making it so that there is only one copy of each characte in the list
    characters = list(set(character))

    #creating a dictionairy with the characters and 0
    for i in characters:
        dic[i] = 0
        
    # filling the dictionairy with the character count
    for i in character:
        dic[i] += 1
 

    return dic
