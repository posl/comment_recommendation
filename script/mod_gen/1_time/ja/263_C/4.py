def main():
    n,m = map(int,input().split())
    ans = []
    for i in range(1,m+1):
        ans.append([i])
    for i in range(n-1):
        tmp = []
        for j in range(len(ans)):
            for k in range(ans[j][-1]+1,m+1):
                tmp.append(ans[j]+[k])
        ans = tmp
    for i in range(len(ans)):
        print(*ans[i])

if __name__ == '__main__':
    main()