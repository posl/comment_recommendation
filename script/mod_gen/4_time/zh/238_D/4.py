def solve(a, s):
    if a > s:
        return "No"
    if a == s:
        return "Yes"
    if (s - a) % 2 == 0:
        return "Yes"
    return "No"
t = int(input())
for i in range(t):
    a, s = map(int, input().split())
    print(solve(a, s))
