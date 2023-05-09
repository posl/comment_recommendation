def main():
    n = int(input())
    a = list(map(int, input().split()))
    a2 = [x**2 for x in a]
    s2 = sum(a2)
    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        s2 -= a2[i]
        ans += s2 - 2 * s * a[i]
    print(ans)

if __name__ == '__main__':
    main()