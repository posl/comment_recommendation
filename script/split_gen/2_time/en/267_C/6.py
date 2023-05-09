def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, M)
    # print(A)
    B = sorted(A, reverse=True)
    # print(B)
    ans = 0
    for i in range(M):
        ans += B[i]
    print(ans)
