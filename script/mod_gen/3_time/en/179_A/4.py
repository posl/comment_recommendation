def plural_form(s):
    if s[-1] == 's':
        print(s + 'es')
    else:
        print(s + 's')
s = input()
plural_form(s)
