def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    ans = [-1]*n
    for i in range(n):
        if i<k:
            ans[p[i]-1] = i+1
        else:
            if ans[p[i]-1] == -1:
                ans[p[i]-1] = ans[p[i-k]-1]
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()