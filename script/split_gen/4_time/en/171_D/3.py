def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    sumA = sum(A)
    cnt = [0] * 100001
    for a in A:
        cnt[a] += 1
    for b, c in BC:
        sumA += (c - b) * cnt[b]
        cnt[c] += cnt[b]
        cnt[b] = 0
        print(sumA)
