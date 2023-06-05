def solve(n,k,x):
    ans = 10**9
    for i in range(n-k+1):
        lx = x[i]
        rx = x[i+k-1]
        time = rx-lx
        if lx<0 and rx<0:
            time -= lx
        elif lx<0 and 0<=rx:
            time += min(abs(lx),rx)
        else:
            time += rx
        ans = min(ans,time)
    return ans
n,k = map(int,input().split())
x = list(map(int,input().split()))
print(solve(n,k,x))
