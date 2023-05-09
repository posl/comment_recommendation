def count(n):
    if n == 1:
        return 9
    elif n == 2:
        return 17
    else:
        return (count(n-1) + count(n-2)) % 998244353
