def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    a = []
    b = []
    for i in range(m):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    #print(n,m,h,a,b)
    ans = 0
    for i in range(m):
        if h[a[i]-1] > h[b[i]-1]:
            ans += 1
        elif h[a[i]-1] < h[b[i]-1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()