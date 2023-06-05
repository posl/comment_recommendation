def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * (2 * 10 ** 5 + 1)
    for i in a:
        c[i] += 1
    ans = 0
    for i in range(1, 2 * 10 ** 5 + 1):
        ans += c[i] // 2
        c[i] = c[i] % 2
    print(2 * ans // 2)

if __name__ == '__main__':
    solve()