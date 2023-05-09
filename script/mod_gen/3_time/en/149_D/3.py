def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    T = list(T)
    for i in range(N):
        if T[i] == 'r':
            T[i] = P
        elif T[i] == 's':
            T[i] = R
        else:
            T[i] = S
    for i in range(K, N):
        if T[i] == T[i-K]:
            T[i] = 0
    print(sum(T))

if __name__ == '__main__':
    main()