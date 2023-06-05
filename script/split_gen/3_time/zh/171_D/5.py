def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    sum_A = sum(A)
    cnt = [0] * (10**5 + 1)
    for a in A:
        cnt[a] += 1
    for b, c in BC:
        sum_A += (c - b) * cnt[b]
        cnt[c] += cnt[b]
        cnt[b] = 0
        print(sum_A)
