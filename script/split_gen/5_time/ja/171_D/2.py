def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    # compute
    sumA = sum(A)
    cnt = [0] * (10**5+1)
    for i in range(10**5+1):
        cnt[i] = A.count(i)
    # output
    for i in range(Q):
        sumA += (BC[i][1] - BC[i][0]) * cnt[BC[i][0]]
        cnt[BC[i][1]] += cnt[BC[i][0]]
        cnt[BC[i][0]] = 0
        print(sumA)
