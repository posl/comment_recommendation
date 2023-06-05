def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    ans = 0
    for i in range(n):
        ans += i - a.index(a[i])
    print(ans)

if __name__ == '__main__':
    main()