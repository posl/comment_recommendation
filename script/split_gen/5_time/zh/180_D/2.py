def main():
    x, y, a, b = map(int, input().split())
    exp = 0
    while x < y:
        if x * a < x + b:
            x *= a
        else:
            x += b
        exp += 1
    print(exp - 1)
