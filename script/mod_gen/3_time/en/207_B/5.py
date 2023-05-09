def solve(a, b, c, d):
    if b >= a * d:
        return -1
    if c <= b:
        return 1
    return (a * d - b + c - b - 1) // (c - b) + 1
a, b, c, d = map(int, input().split())
print(solve(a, b, c, d))
I don't know why but I could not solve this problem by myself. I had to look at the editorial first. I think I should try to solve more problems by myself before I start to look at the editorial.

if __name__ == '__main__':
    solve()