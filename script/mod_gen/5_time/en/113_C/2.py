def main():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        p, y = map(int, input().split())
        if p in d:
            d[p].append([y, i])
        else:
            d[p] = [[y, i]]
    for k in d.keys():
        d[k].sort()
    ans = []
    for k in d.keys():
        for i in range(len(d[k])):
            ans.append([d[k][i][1], str(k).zfill(6) + str(i+1).zfill(6)])
    ans.sort()
    for i in range(len(ans)):
        print(ans[i][1])

if __name__ == '__main__':
    main()