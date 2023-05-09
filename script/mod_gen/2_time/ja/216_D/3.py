def main():
    N, M = map(int, input().split())
    k = list()
    a = list()
    for i in range(M):
        k.append(int(input()))
        a.append(list(map(int, input().split())))
    for i in range(M):
        for j in range(k[i]):
            a[i][j] -= 1
    ball = [0] * N
    for i in range(M):
        for j in range(k[i]):
            ball[a[i][j]] += 1
    for i in range(N):
        if ball[i] % 2 == 1:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()