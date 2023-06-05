def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    ans = [-1]*n
    t = 0
    for i in range(n):
        while t>0 and p[i]>p[ans[t-1]]:
            t -= 1
        ans[t] = i
        t += 1
        if t == k:
            for j in range(k):
                ans[j] = -1
            t = 0
    for i in range(n):
        print(ans[i]+1)

if __name__ == '__main__':
    main()