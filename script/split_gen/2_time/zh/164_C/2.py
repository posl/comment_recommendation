def count_words(words):
    #print(words)
    words_list = words.split()
    #print(words_list)
    return len(set(words_list))
