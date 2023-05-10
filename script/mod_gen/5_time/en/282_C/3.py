def main():
    N = int(input())
    S = input()
    K = int(S.count('"')/2)
    for i in range(1,K+1):
        S = S.replace(',', '.', 1)
    print(S)

if __name__ == '__main__':
    main()