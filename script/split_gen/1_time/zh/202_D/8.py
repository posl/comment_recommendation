def combinations(a, b, k):
    if a == 0:
        return 'b'*b
    elif b == 0:
        return 'a'*a
    elif k <= 2**(a+b-1):
        return 'a' + combinations(a-1, b, k-1)
    else:
        return 'b' + combinations(a, b-1, k-2**(a+b-1))
a, b, k = map(int, input().split())
print(combinations(a, b, k))
