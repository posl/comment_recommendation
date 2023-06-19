def comparePow(a, b, c):
    if pow(a, c) > pow(b, c):
        return ">"
    elif pow(a, c) < pow(b, c):
        return "<"
    else:
        return "="
print(comparePow(3, 2, 4))
print(comparePow(-7, 7, 2))
print(comparePow(-8, 6, 3))
