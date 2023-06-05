def main():
    n,q = map(int,input().split())
    x = []
    for i in range(q):
        x.append(int(input()))
    ans = [i for i in range(1,n+1)]
    for i in range(q-1,-1,-1):
        ans[x[i]-1],ans[x[i]] = ans[x[i]],ans[x[i]-1]
    print(' '.join(map(str,ans)))

if __name__ == '__main__':
    main()