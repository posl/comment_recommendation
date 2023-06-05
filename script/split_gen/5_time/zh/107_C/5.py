def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    #print(n,k)
    #print(x)
    ans = 10**9 + 1
    for i in range(n-k+1):
        left = x[i]
        right = x[i+k-1]
        time = min(abs(left),abs(right)) + right - left
        #print(left,right,time)
        ans = min(ans,time)
    print(ans)
