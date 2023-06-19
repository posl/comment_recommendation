def check(s):
    return s.count('o')
n, x = map(int, input().split())
s = input()
print(x + check(s) - s.count('x'))
