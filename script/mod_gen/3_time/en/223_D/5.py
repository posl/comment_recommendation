def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    P = [-1] * (N + 1)
    for a, b in AB:
        if P[b] == -1:
            P[b] = a
        elif P[b] != a:
            print(-1)
            return
    for i in range(1, N + 1):
        if P[i] == -1:
            P[i] = i
        else:
            P[i] = P[P[i]]
    print(*P[1:])

if __name__ == '__main__':
    main()