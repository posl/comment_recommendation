def main():
    S = input()
    K = int(input())
    S = S.replace('.','X')
    S = S.replace('X','.')
    print(S)
    print(K)

if __name__ == '__main__':
    main()