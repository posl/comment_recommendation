def is_diff(a, b, c):
    if a == b and a != c:
        return True
    elif a == c and a != b:
        return True
    elif b == c and b != a:
        return True
    else:
        return False
a, b, c = map(int, input().split())
