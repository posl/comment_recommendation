def solve():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, L, R)
    # print(A)
    A.sort()
    # print(A)
    ans = 0
    for i in range(N):
        if A[i] < 0:
            if L > 0:
                L -= 1
                ans += -A[i]
            elif R > 0:
                R -= 1
                ans += -A[i]
            else:
                ans += A[i]
        else:
            if R > 0:
                R -= 1
                ans += A[i]
            elif L > 0:
                L -= 1
                ans += A[i]
            else:
                ans += -A[i]
    print(ans)

if __name__ == '__main__':
    solve()