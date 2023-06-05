def main():
    S = input()
    S = S[::-1]
    S = S.replace('6', 'x')
    S = S.replace('9', '6')
    S = S.replace('x', '9')
    S = S.replace('8', 'x')
    S = S.replace('1', 'x')
    S = S.replace('0', '1')
    S = S.replace('x', '0')
    print(S)
