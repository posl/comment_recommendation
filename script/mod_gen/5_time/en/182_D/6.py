def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    s = 0
    for i in range(n):
        s += a[i]
        ans = max(ans, s)
    print(ans)

if __name__ == '__main__':
    main()