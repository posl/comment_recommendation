def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    c = []
    for i in range(m):
        b_i,c_i = map(int,input().split())
        b.append(b_i)
        c.append(c_i)
    a.sort()
    c.sort(reverse=True)
    ans = 0
    j = 0
    for i in range(n):
        if j < m and c[j] > a[i]:
            ans += c[j]
            j += 1
        else:
            ans += a[i]
    print(ans)

if __name__ == '__main__':
    main()