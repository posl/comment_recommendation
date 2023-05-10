def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if i == 0:
            A[i] %= M
        else:
            A[i] = (A[i - 1] + A[i]) % M
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] == 0:
            ans += 1
    for i in range(N):
        if i > 0 and A[i - 1] == A[i]:
            ans += 1
    print(ans)
