def cal(a, b, c):
    return 10 * a + b + c
a, b, c = map(int, input().split())
print(max(cal(a, b, c), cal(b, a, c), cal(c, a, b), cal(a, c, b), cal(b, c, a), cal(c, b, a)))
