def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    ans = 0
    for i in range(n):
        ans += (n-1-2*i)*a[i]
    print(ans)

if __name__ == '__main__':
    main()