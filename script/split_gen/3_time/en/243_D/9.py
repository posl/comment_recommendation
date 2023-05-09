def f(x, s):
    if s == '': return x
    if s[0] == 'U': return f(x//2, s[1:])
    if s[0] == 'L': return f(x//2, s[1:]) * 2
    if s[0] == 'R': return f(x//2, s[1:]) * 2 + 1
n, x = map(int, input().split())
s = input()
print(f(x, s))
