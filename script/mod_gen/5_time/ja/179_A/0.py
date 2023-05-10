def plural_form():
    s = input()
    if s[-1] == 's':
        print(s + 'es')
    else:
        print(s + 's')

if __name__ == '__main__':
    plural_form()