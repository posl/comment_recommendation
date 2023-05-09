def problems101_c():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    while N > K:
        N -= K - 1
        cnt += 1
    if N > 1:
        cnt += 1
    print(cnt)
problems101_c()

if __name__ == '__main__':
    problems101_c()