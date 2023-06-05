def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    dic = {}
    for i in range(n):
        if a[i] in dic:
            dic[a[i]] = dic[a[i]] + 1
        else:
            dic[a[i]] = 1
    #print(dic)
    #print(a)
    #print(n,k)
    ans = 0
    for i in range(n):
        if dic[a[i]] >= k:
            ans = ans + 1
            dic[a[i]] = dic[a[i]] - k
        else:
            k = k - dic[a[i]]
            dic[a[i]] = 0
    print(ans)

if __name__ == '__main__':
    main()