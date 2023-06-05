def solve():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n - 1):
        if s[i] == "R" and s[i + 1] == "L":
            if (i + 1) % 2 == 0:
                ans[i + 1] += 1
            else:
                ans[i] += 1
    for i in range(n):
        if s[i] == "R":
            x = i + 1
            while x < n and s[x] == "R":
                x += 1
            if (i + 1) % 2 == 0:
                ans[x] += (x - i) // 2
                ans[x - 1] += (x - i) // 2 + (x - i) % 2
            else:
                ans[x] += (x - i) // 2 + (x - i) % 2
                ans[x - 1] += (x - i) // 2
            i = x - 1
    for i in range(n - 1, -1, -1):
        if s[i] == "L":
            x = i - 1
            while x >= 0 and s[x] == "L":
                x -= 1
            if (i + 1) % 2 == 0:
                ans[x] += (i - x) // 2
                ans[x + 1] += (i - x) // 2 + (i - x) % 2
            else:
                ans[x] += (i - x) // 2 + (i - x) % 2
                ans[x + 1] += (i - x) // 2
            i = x + 1
    for i in range(n):
        print(ans[i], end=" ")
    print()

if __name__ == '__main__':
    solve()