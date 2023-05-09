def plural_form(S):
    if S.endswith('s'):
        return S + 'es'
    else:
        return S + 's'

if __name__ == '__main__':
    plural_form()