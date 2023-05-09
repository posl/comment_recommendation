def solve():
    N = int(input())
    A = list(map(int,input().split()))
    if A[0] != 1:
        print(-1)
        return
    else:
        ans = 0
        for i in range(1,N):
            if A[i] == A[i-1]+1:
                continue
            elif A[i] > A[i-1]+1:
                print(-1)
                return
            else:
                ans += 1
        print(ans)

if __name__ == '__main__':
    solve()