def f(x, m):
    d = int(max(x))
    ans = 0
    while True:
        if int(x, d+1) <= m:
            ans += 1
        else:
            break
        d += 1
    return ans
x = input()
m = int(input())
print(f(x, m))
