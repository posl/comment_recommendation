def solve():
    N,K = map(int,input().split())
    S = input()
    l = 0
    r = 0
    ans = 0
    count = 0
    while l < N:
        while r < N and (r == l or (r < N and S[r] == S[r-1])):
            r += 1
        if S[l] == '0':
            count += r - l
        ans = max(ans,r - l)
        l += 1
    if K > 0:
        ans = min(ans,N)
    else:
        ans = min(ans,count)
    print(ans)

if __name__ == '__main__':
    solve()