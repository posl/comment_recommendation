def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    ans = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                ans += a.count(i+1) * b.count(j+1)
    print(ans)

if __name__ == '__main__':
    main()