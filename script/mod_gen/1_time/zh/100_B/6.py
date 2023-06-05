def find_number(d, n):
    if d == 0:
        return n
    elif d == 1:
        return n * 100
    else:
        return n * 10000
d, n = map(int, input().split())
print(find_number(d, n))
