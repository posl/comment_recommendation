def pluralize(noun):
    if noun.endswith('s'):
        return noun + 'es'
    else:
        return noun + 's'
