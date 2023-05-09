def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        if K & (1 << i) == 0:
            continue
        B = [a & ((1 << i) - 1) for a in A]
        B.sort()
        if (sum(B) + (N - sum(1 for b in B if b == 0)) * (1 << i)) // 2 <= K:
            ans += (1 << i)
            A = [a ^ (1 << i) for a in A]
    print(ans + sum(A))
