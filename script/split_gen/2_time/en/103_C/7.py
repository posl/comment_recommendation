def solve():
    N = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = a[-1]
    for i in range(1,N):
        ans += a[-1-i]-1
    return ans
print(solve())
