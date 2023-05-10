def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    d = [0]*(n+1)
    for i in range(n):
        d[a[i]] += 1
    for i in range(1,n+1):
        ans += d[i]*(d[i]-1)//2
    print(ans)

if __name__ == '__main__':
    main()