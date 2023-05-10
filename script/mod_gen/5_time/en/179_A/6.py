def plural_form(S):
    if S[-1] == 's':
        return S + 'es'
    else:
        return S + 's'

if __name__ == '__main__':
    plural_form()