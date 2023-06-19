def main():
    S = input()
    S = S[::-1]
    S = S.replace('6', 'T')
    S = S.replace('9', '6')
    S = S.replace('T', '9')
    S = S.replace('0', 'T')
    S = S.replace('1', '0')
    S = S.replace('T', '1')
    print(S)
