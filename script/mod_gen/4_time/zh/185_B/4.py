def main():
    n,m,t = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    a.insert(0,0)
    b.insert(0,0)
    a.append(t)
    b.append(t)
    ans = 'Yes'
    for i in range(m+1):
        n -= a[i+1] - b[i]
        if n <= 0:
            ans = 'No'
            break
        n += b[i+1] - a[i+1]
        if n > 10**9:
            n = 10**9
    print(ans)

if __name__ == '__main__':
    main()