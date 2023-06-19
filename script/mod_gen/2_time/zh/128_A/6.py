def max_pie(a, p):
    return (a * 3 + p) // 2
a, p = map(int, input().split())
print(max_pie(a, p))
