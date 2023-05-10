def main():
    N,K = map(int,input().split())
    c = list(map(int,input().split()))
    ans = 0
    dic = {}
    for i in range(K):
        if c[i] in dic:
            dic[c[i]] += 1
        else:
            dic[c[i]] = 1
    ans = len(dic)
    for i in range(K,N):
        if c[i] in dic:
            dic[c[i]] += 1
        else:
            dic[c[i]] = 1
        dic[c[i-K]] -= 1
        if dic[c[i-K]] == 0:
            del dic[c[i-K]]
        ans = max(ans,len(dic))
    print(ans)
