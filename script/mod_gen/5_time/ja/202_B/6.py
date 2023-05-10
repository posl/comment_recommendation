def main():
    S = input()
    S = S[::-1]
    S = S.replace('6','X')
    S = S.replace('9','6')
    S = S.replace('X','9')
    print(S)

if __name__ == '__main__':
    main()