def plural_form(s):
    if s.endswith('s'):
        return s + 'es'
    return s + 's'

if __name__ == '__main__':
    plural_form()