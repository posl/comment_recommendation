def distinct_integers():
    a, b, c, d, e = map(int, input().split())
    return len(set([a, b, c, d, e]))
print(distinct_integers())

if __name__ == '__main__':
    distinct_integers()