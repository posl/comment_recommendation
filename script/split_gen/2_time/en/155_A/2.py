def poor(a, b, c):
    if a == b and a != c:
        return 'Yes'
    elif a == c and a != b:
        return 'Yes'
    elif b == c and b != a:
        return 'Yes'
    else:
        return 'No'
