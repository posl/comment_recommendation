def solve():
    # x,y = map(int, input().split())
    x, y = 270, 750
    ans = 0
    if x == y:
        return ans
    if x > y:
        return ans
    if x < y:
        if x % 10 == 0:
            ans = (y - x) // 10
        else:
            ans = (y - x) // 10 + 1
    return ans
print(solve())

if __name__ == '__main__':
    solve()