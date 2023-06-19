def recursion(n):
    if n == 1:
        return [1]
    else:
        l = recursion(n-1)
        return l + [n] + l
n = int(input())
print(*recursion(n))
