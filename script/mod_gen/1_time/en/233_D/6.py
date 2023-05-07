def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    d = {0:1}
    for i in range(n):
        s += a[i]
        ans += d.get(s-k,0)
        d[s] = d.get(s,0)+1
    print(ans)
main()

if __name__ == '__main__':
    main()