def pluralize(word):
    if word.endswith('s'):
        return word + 'es'
    else:
        return word + 's'
