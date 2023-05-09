def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print('No')
        return
    d = [0] * N
    for _ in range(M):
        u, v = map(int, input().split())
        d[u - 1] += 1
        d[v - 1] += 1
    for i in range(N):
        if d[i] != 2:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()