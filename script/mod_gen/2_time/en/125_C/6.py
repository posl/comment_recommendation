def main():
    n = int(input())
    a = list(map(int,input().split()))
    if n == 2:
        print(max(a))
        return
    a.sort()
    if a[0] == a[1]:
        print(a[0])
        return
    g = a[1]
    for i in range(2,n):
        g = gcd(g,a[i])
    print(g)

if __name__ == '__main__':
    main()