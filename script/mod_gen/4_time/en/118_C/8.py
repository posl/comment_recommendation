def solve():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        if A[i]*2 < A[i+1]:
            ans = i+1
    print(N-ans)

if __name__ == '__main__':
    solve()