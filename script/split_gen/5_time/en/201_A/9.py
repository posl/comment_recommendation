def is_arithmetic_sequence(a):
    if a[0] - a[1] == 0 or a[1] - a[2] == 0:
        return True
    elif a[0] - a[1] == a[1] - a[2]:
        return True
    else:
        return False
a = list(map(int, input().split()))
