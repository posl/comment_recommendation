def print_alphabet(P):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in P:
        result += alphabet[i-1]
    return result
