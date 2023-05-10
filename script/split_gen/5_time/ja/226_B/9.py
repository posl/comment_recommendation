def main():
    N = int(input())
    L = [0] * N
    A = [0] * N
    for i in range(N):
        L[i], *A[i] = map(int, input().split())
    A.sort()
    ans = 1
    for i in range(1, N):
        if A[i] != A[i-1]:
            ans += 1
    print(ans)
