def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(1 << N):
        if bin(i).count('1') == K:
            s = 0
            for j in range(N):
                if (i >> j) & 1:
                    s += A[j]
            S.add(s)
    ans = max([i for i in S if i % D == 0] or [-1])
    print(ans)
