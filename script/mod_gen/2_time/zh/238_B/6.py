def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for i in range(1, n):
        if a[i] - a[i-1] < 0:
            a[i] += 360
    a.sort()
    for i in range(n):
        ans = max(ans, a[i] - a[i-1])
    print(360 - ans)

if __name__ == '__main__':
    main()