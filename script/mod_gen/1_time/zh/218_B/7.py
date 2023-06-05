def print_alphabet(P):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in P:
        result += alphabet[i-1]
    return result

if __name__ == '__main__':
    print_alphabet()