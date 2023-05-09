def pluralize(word):
    if word[len(word)-1] == 's':
        word += 'es'
    else:
        word += 's'
    return word
