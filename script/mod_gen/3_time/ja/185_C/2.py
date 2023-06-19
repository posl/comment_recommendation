def calc_cut(n):
    if n == 12:
        return 1
    else:
        return calc_cut(n-1) + (n-1)
n = int(input())
print(calc_cut(n))
