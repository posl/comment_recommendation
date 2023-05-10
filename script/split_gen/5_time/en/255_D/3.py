def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    A.append(10**9+1)
    X.append(0)
    ans = 0
    for i in range(N):
        ans += abs(A[i] - A[i+1])
    for x in X:
        for i in range(N):
            if A[i] <= x <= A[i+1]:
                ans -= abs(A[i] - x)
                ans += abs(A[i+1] - x)
                break
        print(ans)
