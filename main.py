def naive_string_search(text, word):
    return search_word(0, text, word)
    
def search_word(initial_index, text, word):
    step = 3
    
    if(word == text[initial_index:initial_index + step]):
        return initial_index
    elif(initial_index + step > len(text)):
        return -1
    else:
        return search_word(initial_index + 1, text, word)

print(naive_string_search("ABCDCBDCBDACBDABDCBADF", "ADF"))