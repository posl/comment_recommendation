def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    A.sort()
    s = [0] * (N+1)
    for i in range(N):
        s[i+1] = s[i] + A[i]
    for i in range(Q):
        left = 0
        right = N-1
        while left < right:
            mid = (left + right) // 2
            if A[mid] >= X[i]:
                right = mid
            else:
                left = mid + 1
        print(N* X[i] - s[left] - (N-left) * X[i])
