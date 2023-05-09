def plural_form(string):
    if string.endswith('s'):
        return string + 'es'
    else:
        return string + 's'
