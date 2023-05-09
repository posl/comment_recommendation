def plural_form(s):
    if s.endswith('s'):
        print(s + 'es')
    else:
        print(s + 's')

if __name__ == '__main__':
    plural_form()