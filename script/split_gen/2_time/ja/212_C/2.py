def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    a = 0
    b = 0
    ans = 10 ** 9
    while a < N and b < M:
        ans = min(ans, abs(A[a] - B[b]))
        if A[a] < B[b]:
            a += 1
        else:
            b += 1
    print(ans)
