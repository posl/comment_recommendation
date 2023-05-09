def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    S = set()
    for i in range(M):
        u, v = map(int, input().split())
        S.add((u, v))
        S.add((v, u))
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if (i, j) not in S:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()