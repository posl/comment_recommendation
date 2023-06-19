def solve():
    n,k = map(int,input().split())
    #print(n,k)
    p = 0
    for i in range(1,n+1):
        if i >= k:
            p += 1/n
        else:
            c = 1
            while i < k:
                i *= 2
                c /= 2
            p += c/n
    print(p)

if __name__ == '__main__':
    solve()