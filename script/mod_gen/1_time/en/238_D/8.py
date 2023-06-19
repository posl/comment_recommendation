def solve(a, s):
    x = (s - a) // 2
    y = (s + a) // 2
    if x + y == s and x & y == a:
        return "Yes"
    else:
        return "No"
t = int(input())
for i in range(t):
    a, s = map(int, input().split())
    print(solve(a, s))
