def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0:
            if a[i] == a[i + 1]:
                ans += 1
        elif i == n - 1:
            if a[i] == a[i - 1]:
                ans += 1
        else:
            if a[i] == a[i - 1] or a[i] == a[i + 1]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()