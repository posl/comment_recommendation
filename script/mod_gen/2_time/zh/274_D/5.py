def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0,0)
    ans = [0] * (2 * n + 1)
    for i in range(1, n + 1):
        ans[i] = 1
    for i in range(n, 0, -1):
        ans[i] += max(ans[2 * i], ans[2 * i + 1])
    for i in range(1, 2 * n + 1):
        print(ans[i])

if __name__ == '__main__':
    main()