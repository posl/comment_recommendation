def pluralize(word):
    if word.endswith('s'):
        return word + 'es'
    else:
        return word + 's'

if __name__ == '__main__':
    pluralize()