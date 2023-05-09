def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    ans = 0
    count = 0
    dic = {}
    for i in range(k):
        if c[i] in dic:
            dic[c[i]] += 1
        else:
            dic[c[i]] = 1
            count += 1
    ans = count
    for i in range(n-k):
        dic[c[i]] -= 1
        if dic[c[i]] == 0:
            count -= 1
        if c[i+k] in dic:
            dic[c[i+k]] += 1
        else:
            dic[c[i+k]] = 1
            count += 1
        ans = max(ans,count)
    print(ans)

if __name__ == '__main__':
    main()