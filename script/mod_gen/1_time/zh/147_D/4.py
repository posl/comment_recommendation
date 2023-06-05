def solve():
    #N = int(input())
    #A = list(map(int, input().split()))
    N = 3
    A = [1,2,3]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans += A[i]^A[j]
    print(ans)
    return 0

if __name__ == '__main__':
    solve()