def main():
    n,m = map(int,input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int,input().split())
    ans = 0
    #print(a)
    #print(b)
    for i in range(n):
        if m <= b[i]:
            ans += a[i] * m
            break
        else:
            ans += a[i] * b[i]
            m -= b[i]
    print(ans)

if __name__ == '__main__':
    main()