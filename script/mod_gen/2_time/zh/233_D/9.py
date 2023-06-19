def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i]+a[i])
    s.sort()
    ans = 0
    for i in range(n):
        ans += len([x for x in s if x == k + s[i]])
    print(ans)

if __name__ == '__main__':
    main()