def main():
    N, M = map(int, input().split())
    P = [i for i in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        a = P[a]
        b = P[b]
        if a > b:
            a, b = b, a
        P[a] = b
        P[b] = b
    for i in range(1, N + 1):
        if P[i] != P[i + 1]:
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    main()