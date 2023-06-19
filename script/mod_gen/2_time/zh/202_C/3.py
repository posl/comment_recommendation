def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    c.sort()
    ans = 0
    for i in range(n):
        ans += bisect.bisect_left(a, b[c[i]-1])*(n-bisect.bisect_right(b, b[c[i]-1]))
    print(ans)

if __name__ == '__main__':
    main()