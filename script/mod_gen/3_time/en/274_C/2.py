def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i] - 1] = ans[(a[i] - 1) // 2] + 1
    for i in range(2 * n + 1):
        print(ans[i])

if __name__ == '__main__':
    main()