def main():
    a, b, c, x = map(int, input().split())
    if x <= a:
        print(1)
    elif x > b:
        print(0)
    else:
        print((b - x + 1) / (b - a + 1))
