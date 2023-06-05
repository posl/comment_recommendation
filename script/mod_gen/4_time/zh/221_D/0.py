def solve():
    n = int(input())
    days = []
    for i in range(n):
        a, b = map(int, input().split())
        days.append((a, 1))
        days.append((a + b, -1))
    days.sort()
    ans = [0] * (n + 1)
    num = 0
    last = 0
    for day, diff in days:
        ans[num] += day - last
        num += diff
        last = day
    print(*ans[1:])

if __name__ == '__main__':
    solve()