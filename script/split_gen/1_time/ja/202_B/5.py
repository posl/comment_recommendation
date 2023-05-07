def main():
    S = input()
    S = S[::-1]
    S = S.replace('0', 't')
    S = S.replace('1', 'o')
    S = S.replace('6', 'n')
    S = S.replace('8', 'e')
    S = S.replace('9', 's')
    S = S.replace('t', '9')
    S = S.replace('o', '1')
    S = S.replace('n', '6')
    S = S.replace('e', '8')
    S = S.replace('s', '0')
    print(S)
