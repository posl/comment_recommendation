def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(1, n):
        ans += a[i] - a[i - 1]
    print(ans * 2)

if __name__ == '__main__':
    main()