def seq(n):
    if n == 1:
        return [1]
    else:
        return seq(n-1) + [n] + seq(n-1)
n = int(input())
for i in seq(n):
    print(i, end=' ')
