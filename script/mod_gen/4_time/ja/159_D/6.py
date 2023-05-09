def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0 for _ in range(n+1)]
    for i in range(n):
        cnt[a[i]] += 1
    ans = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        ans[i] = cnt[i] * (cnt[i]-1) // 2
    allsum = sum(ans)
    for i in range(n):
        print(allsum - (cnt[a[i]]-1))

if __name__ == '__main__':
    main()