def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    cnt = 0
    for a in A:
        tmp = 0
        for i in range(M):
            tmp += a[i] * B[i]
        if tmp + C > 0:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()