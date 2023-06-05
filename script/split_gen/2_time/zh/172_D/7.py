def main():
    n, m, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a = sorted(a)
    b = sorted(b)
    if len(a) > len(b):
        a, b = b, a
    i = 0
    j = 0
    while i < len(a) and k >= a[i]:
        k -= a[i]
        i += 1
    while j < len(b) and k >= b[j]:
        k -= b[j]
        j += 1
    print(i + j)
