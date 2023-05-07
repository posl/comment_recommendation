def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 0:
        print(sum(A))
        return
    ans = 0
    for i in range(1, N):
        if A[i] == A[i-1]:
            continue
        if A[i] == A[i-1] + 1:
            continue
        ans += A[i-1]
    ans += A[-1]
    print(ans)
