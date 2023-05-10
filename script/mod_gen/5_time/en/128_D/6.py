def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    k = min(n, k)
    for i in range(k+1):
        for j in range(k+1-i):
            l = v[:i] + v[n-j:]
            l.sort()
            ans = max(ans, sum(l[j:]))
    print(ans)

if __name__ == '__main__':
    main()