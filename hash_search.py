def hash(word, word_size):
    hash_value = 0
    Q = 71

    for i in range(word_size):
        hash_value = (hash_value * 26 + ord(word[i])) % Q


    return hash_value

def search(text, word):
    text_size = len(text)
    word_size = len(word)
    hash_word = hash(word, word_size)
    
    for i in range(text_size-word_size):
        hash_text = hash(text[i:i+word_size], word_size)

        if(hash_text == hash_word):
            return True


print(search("ABCDCBDCBDACBDABDCBADF", "ADF"))
