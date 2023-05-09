def main():
    S = input()
    S = S[::-1]
    S = S.replace('6','x')
    S = S.replace('9','6')
    S = S.replace('x','9')
    print(S)
