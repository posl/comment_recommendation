def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    #print(n,k)
    #print(c)
    d = {}
    for i in range(k):
        if c[i] in d:
            d[c[i]] += 1
        else:
            d[c[i]] = 1
    #print(d)
    ans = len(d)
    for i in range(n-k):
        #print(i)
        if d[c[i]] == 1:
            del d[c[i]]
        else:
            d[c[i]] -= 1
        if c[i+k] in d:
            d[c[i+k]] += 1
        else:
            d[c[i+k]] = 1
        #print(d)
        ans = max(ans,len(d))
    print(ans)
