def main():
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a**2 + b**2 < c**2:
        print('Yes')
    else:
        print('No')
