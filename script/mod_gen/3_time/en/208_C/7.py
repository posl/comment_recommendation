def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.insert(0,0)
    ans = []
    for i in range(N):
        ans.append(K//(N-i))
        K -= K//(N-i)
    for i in range(N):
        if K == 0:
            break
        if a[i+1] - a[i] <= K:
            ans[i] += a[i+1] - a[i]
            K -= a[i+1] - a[i]
        else:
            ans[i] += K
            K = 0
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()