def sort_by_lexicographical_order(s, x):
    y = list(s)
    for i in range(len(y)):
        y[i] = chr(ord('a') + x.index(y[i]))
    return ''.join(y)
x = input()
n = int(input())
s = []
for i in range(n):
    s.append(input())
s.sort(key = lambda x: sort_by_lexicographical_order(x, x))
for i in range(n):
    print(s[i])
