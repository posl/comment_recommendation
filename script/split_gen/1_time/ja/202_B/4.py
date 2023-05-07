def main():
    S = input()
    S = S[::-1]
    S = S.replace('0','o')
    S = S.replace('1','i')
    S = S.replace('6','9')
    S = S.replace('8','8')
    S = S.replace('9','6')
    S = S.replace('o','0')
    S = S.replace('i','1')
    print(S)
