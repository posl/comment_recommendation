def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    m = A[-1] + 1
    p = [0] * m
    for i in range(N):
        while A[i] <= m:
            p[A[i]] += 1
            A[i] += A[i]
    ans = 0
    for i in range(N):
        if p[A[i]] == 1:
            ans += 1
    print(ans)
