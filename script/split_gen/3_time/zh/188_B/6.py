def dot_product(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
