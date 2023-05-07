def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])
    for x in X:
        l = 0
        r = N
        while r - l > 1:
            c = (l + r) // 2
            if A[c] < x:
                l = c
            else:
                r = c
        ans = 0
        ans += S[l]
        ans += (N - l) * x
        print(ans)
