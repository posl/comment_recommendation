def find(s):
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                return [i, j]
s = []
for i in range(10):
    s.append(list(input()))
x, y = find(s)
A = x + 1
C = y + 1
x, y = find(s[::-1])
B = 10 - x
D = 10 - y
print(A, B)
print(C, D)
