def shift_alphabet(s, n):
    if s.isalpha():
        if ord(s) + n <= ord("Z"):
            return chr(ord(s) + n)
        else:
            return chr(ord(s) + n - 26)
    else:
        return s

if __name__ == '__main__':
    shift_alphabet()