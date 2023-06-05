def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    dic = {}
    for i in c[:k]:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    ans = len(dic)
    for i in range(k, n):
        dic[c[i]] = dic.get(c[i], 0) + 1
        dic[c[i-k]] -= 1
        if dic[c[i-k]] == 0:
            del dic[c[i-k]]
        ans = max(ans, len(dic))
    print(ans)

if __name__ == '__main__':
    main()