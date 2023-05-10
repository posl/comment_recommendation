def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    sumA = sum(A)
    cnt = [0] * 100001
    for i in range(N):
        cnt[A[i]] += 1
    for i in range(Q):
        sumA = sumA + (BC[i][1] - BC[i][0]) * cnt[BC[i][0]]
        cnt[BC[i][1]] += cnt[BC[i][0]]
        cnt[BC[i][0]] = 0
        print(sumA)

if __name__ == '__main__':
    main()