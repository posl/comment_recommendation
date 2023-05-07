def main():
    a, b, c, x = map(int, input().split())
    if x < a:
        print(0)
    elif x >= a and x <= b:
        print(c / (b - a + 1))
    else:
        print(1)
