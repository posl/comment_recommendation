def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] != A[i-1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()