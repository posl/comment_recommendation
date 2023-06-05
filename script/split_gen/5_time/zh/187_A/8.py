def S(n):
    n_str = str(n)
    sum = 0
    for i in n_str:
        sum += int(i)
    return sum
a, b = input().split()
a = int(a)
b = int(b)
print(max(S(a), S(b)))
