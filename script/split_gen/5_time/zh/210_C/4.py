def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    #print(n,k,c)
    ans = 0
    s = set()
    for i in range(k):
        s.add(c[i])
    ans = len(s)
    for i in range(k,n):
        s.add(c[i])
        s.remove(c[i-k])
        ans = max(ans,len(s))
    print(ans)
