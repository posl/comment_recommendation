def main():
    N, M = map(int, input().split())
    k = [0] * M
    a = [0] * M
    for i in range(M):
        k[i] = int(input())
        a[i] = list(map(int, input().split()))
    for i in range(M):
        for j in range(k[i]):
            a[i][j] -= 1
    d = [0] * (N + 1)
    for i in range(M):
        d[a[i][0]] += 1
    for i in range(N):
        if d[i] % 2 == 1:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()