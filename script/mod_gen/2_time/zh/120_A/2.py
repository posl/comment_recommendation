def binary_search(s, t, x):
    # 二分查找
    # s, t: list, x: int
    if s[-1] <= x:
        return abs(t[0] - x)
    elif t[-1] <= x:
        return abs(s[0] - x)
    else:
        left = 0
        right = len(s) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if s[mid] < x:
                left = mid
            else:
                right = mid
        return min(abs(s[left] - x) + abs(t[0] - s[left]), abs(s[right] - x) + abs(t[0] - s[right]))

if __name__ == '__main__':
    binary_search()