def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = [0] * n
    ans[0] = s
    for i in range(n - 1):
        ans[i + 1] = a[i] - ans[i] // 2
    print(*ans)

if __name__ == '__main__':
    main()