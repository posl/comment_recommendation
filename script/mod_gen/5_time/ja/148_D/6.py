def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] != 1:
        print(-1)
        return
    ans = 0
    for i in range(1, N):
        if A[i] == A[i-1] + 1:
            pass
        elif A[i] == A[i-1]:
            ans += 1
        else:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    solve()