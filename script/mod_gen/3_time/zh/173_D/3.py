def solve():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    A.insert(0,0)
    ans = 0
    for i in range(1,N):
        ans += A[i//2+1]
    print(ans)

if __name__ == '__main__':
    solve()