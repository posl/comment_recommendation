def f(s):
    if not s:
        return 0
    if s[0] == '0':
        return f(s[1:])
    else:
        return 2*f(s[1:]) + 1
k = int(input())
s = ''
while k > 0:
    if k%2 == 0:
        s = '0' + s
        k = k//2
    else:
        s = '2' + s
        k = (k-1)//2
print(s)
