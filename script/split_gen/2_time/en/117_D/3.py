def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    X = 0
    for i in range(50, -1, -1):
        if X + (1 << i) <= K:
            X += (1 << i)
            if (N - 1) % 2 == 0:
                if A[0] & (1 << i) == 0:
                    A = [a ^ X for a in A]
                    A.sort()
    ans = 0
    for a in A:
        ans += a ^ X
    print(ans)
