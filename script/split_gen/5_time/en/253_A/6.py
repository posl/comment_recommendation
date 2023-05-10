def median(a, b, c):
    if b > a and b < c:
        return True
    elif b < a and b > c:
        return True
    return False
print("Yes" if median(*map(int, input().split())) else "No")
