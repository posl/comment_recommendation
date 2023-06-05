def solve():
    s = input()
    # 从左到右的颜色
    left = [0] * (len(s) + 1)
    # 从右到左的颜色
    right = [0] * (len(s) + 1)
    for i in range(len(s)):
        left[i + 1] = left[i] + int(s[i])
        right[i + 1] = right[i] + int(s[len(s) - i - 1])
    res = len(s)
    for i in range(len(s) + 1):
        res = min(res, left[i] + right[len(s) - i])
    print(res)

if __name__ == '__main__':
    solve()