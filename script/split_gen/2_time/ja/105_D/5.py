def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A.insert(0, 0)
    for i in range(1, N+1):
        A[i] = (A[i] + A[i-1]) % M
    from collections import Counter
    cnt = Counter(A)
    ans = 0
    for k, v in cnt.items():
        ans += v * (v-1) // 2
    print(ans)
