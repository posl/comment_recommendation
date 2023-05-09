def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    ans = 10**9
    while i < N and j < M:
        ans = min(ans, abs(A[i] - B[j]))
        if A[i] > B[j]:
            j += 1
        else:
            i += 1
    print(ans)
