def plural_form(string):
    if string.endswith('s'):
        return string + 'es'
    else:
        return string + 's'

if __name__ == '__main__':
    plural_form()