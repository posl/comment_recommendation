def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = [0] + A
    B = [0] + B
    ans = 0
    for i in range(1, N+1):
        ans += min(A[i], X) * i
        X -= min(A[i], X)
        ans += min(B[i], X) * i
        X -= min(B[i], X)
    print(ans)
