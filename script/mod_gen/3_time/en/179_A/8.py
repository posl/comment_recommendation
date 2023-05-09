def pluralize_word(word):
    if word[-1] == 's':
        return word + 'es'
    else:
        return word + 's'

if __name__ == '__main__':
    pluralize_word()