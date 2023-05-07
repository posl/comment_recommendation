def main():
    S = input()
    S = S[::-1]
    S = S.replace('6','9')
    S = S.replace('9','6')
    print(S)

if __name__ == '__main__':
    main()