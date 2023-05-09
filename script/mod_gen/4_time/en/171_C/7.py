def n_to_alphabet(n):
    if n <= 26:
        return chr(96+n)
    else:
        return n_to_alphabet((n-1)//26) + chr(96+(n-1)%26+1)

if __name__ == '__main__':
    n_to_alphabet()