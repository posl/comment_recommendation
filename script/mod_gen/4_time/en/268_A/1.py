def distinct_integers():
    a, b, c, d, e = map(int, input().split())
    return len(set([a, b, c, d, e]))
print(distinct_integers())
