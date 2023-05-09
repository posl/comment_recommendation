def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0 for i in range(n)]
    ans[0] = sum(a) - 2 * sum(a[1::2])
    for i in range(n-1):
        ans[i+1] = 2 * a[i] - ans[i]
    print(*ans)

if __name__ == '__main__':
    main()