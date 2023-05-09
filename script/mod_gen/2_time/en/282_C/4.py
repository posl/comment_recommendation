def main():
    N = int(input())
    S = input()
    S = S.replace('"', '')
    S = S.replace(',', '.')
    print(S)

if __name__ == '__main__':
    main()