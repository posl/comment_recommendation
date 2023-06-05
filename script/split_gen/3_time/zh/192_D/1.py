def f(x, m):
    d = int(max(x))
    if len(x) == 1:
        return 1 if d <= m else 0
    ans = 0
    for i in range(d+1, 11):
        ans += int(x[0]) * (i ** (len(x)-1))
    if len(x) == 2:
        return ans if ans <= m else ans - 1
    return ans + f(x[1:], m)
x = input()
m = int(input())
print(f(x, m))
