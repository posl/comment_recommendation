def main():
    N, M, X, T, D = map(int, input().split())
    for i in range(M):
        if X <= i:
            T += D
    print(T)

if __name__ == '__main__':
    main()