def main():
    r, x, y = map(int, input().split())
    if (x * x + y * y) % (r * r) == 0:
        print((x * x + y * y) // (r * r))
    else:
        print((x * x + y * y) // (r * r) + 1)
