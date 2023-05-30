def inner_rating(n, r):
    if n >= 10:
        return r
    else:
        return r - (100 * (10 - n))
n, r = map(int, input().split())
print(inner_rating(n, r))
