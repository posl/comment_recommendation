def main():
    S = input()
    S = S[::-1]
    S = S.replace('6', 'a')
    S = S.replace('9', '6')
    S = S.replace('a', '9')
    S = S.replace('1', 'a')
    S = S.replace('0', '1')
    S = S.replace('a', '0')
    print(S)
