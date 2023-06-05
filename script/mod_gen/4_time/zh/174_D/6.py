def solve():
    n = int(input())
    s = input()
    left = 0
    right = n - 1
    ans = 0
    while True:
        while left < n and s[left] == 'R':
            left += 1
        while right >= 0 and s[right] == 'W':
            right -= 1
        if left >= right:
            break
        ans += 1
        left += 1
        right -= 1
    print(ans)

if __name__ == '__main__':
    solve()