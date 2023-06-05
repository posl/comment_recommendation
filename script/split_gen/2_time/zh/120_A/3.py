def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        ans = 10 ** 11
        for j in range(A):
            for k in range(B):
                ans = min(ans, abs(x[i] - s[j]) + abs(s[j] - t[k]))
                ans = min(ans, abs(x[i] - t[k]) + abs(t[k] - s[j]))
        print(ans)
