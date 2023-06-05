def get_num(n, a, b):
    #print(n, a, b)
    if n == 1:
        return b[0] - a[0] + 1
    else:
        return get_num(n-1, a[:-1], b[:-1]) + b[-1] - a[-1] + 1
n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
print(get_num(n, a, b) % 998244353)
