def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    a.sort()
    b.sort()
    c.sort()
    ans = 0
    for i in range(n):
        ans += (bisect.bisect_left(a,b[i])) * (n - bisect.bisect_right(c,b[i]))
    print(ans)

if __name__ == '__main__':
    main()