def plural_form():
    string = input()
    if string.endswith('s'):
        print(string + 'es')
    else:
        print(string + 's')
