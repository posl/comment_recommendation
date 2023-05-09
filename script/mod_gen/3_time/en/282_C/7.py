def main():
    N = int(input())
    S = input()
    K = N//2
    for i in range(K):
        S = S.replace(',','.',1)
    print(S)

if __name__ == '__main__':
    main()