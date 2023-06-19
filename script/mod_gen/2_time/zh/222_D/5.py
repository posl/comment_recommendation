def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mod = 998244353
    ans = 1
    for i in range(N):
        if A[i] > B[i]:
            print(0)
            return
        elif A[i] == B[i]:
            continue
        else:
            ans *= (B[i] - A[i] + 1)
            ans %= mod
    print(ans)

if __name__ == '__main__':
    solve()