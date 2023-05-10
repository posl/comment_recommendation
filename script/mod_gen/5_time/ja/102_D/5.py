def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    s1 = 0
    s2 = 0
    ans = 10**10
    for i in range(n-1):
        s1 += a[i]
        s2 = s - s1
        ans = min(ans, abs(s1-s2))
    print(ans)

if __name__ == '__main__':
    main()