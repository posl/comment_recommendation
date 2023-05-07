def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(k):
        ans += (p[i]+1)/2
    tmp = ans
    for i in range(k,n):
        tmp -= (p[i-k]+1)/2
        tmp += (p[i]+1)/2
        ans = max(ans,tmp)
    print(ans)
