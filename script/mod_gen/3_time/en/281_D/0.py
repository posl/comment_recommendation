def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(1 << N):
        if bin(i).count("1") != K:
            continue
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += A[j]
        S.add(s)
    ans = -1
    for s in S:
        if s % D == 0:
            ans = max(ans, s)
    print(ans)
main()
