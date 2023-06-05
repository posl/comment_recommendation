def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    s = set()
    for i in range(n-k+1):
        for j in range(i,i+k):
            s.add(a[j])
        ans = max(ans,len(s))
        s.clear()
    print(ans)
