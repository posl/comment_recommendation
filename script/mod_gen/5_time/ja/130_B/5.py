def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i] + l[i])
    ans = 0
    for i in range(n+1):
        if d[i] <= x:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()