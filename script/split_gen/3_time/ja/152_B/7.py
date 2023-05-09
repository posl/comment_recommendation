def main():
    a, b = map(int, input().split())
    if a * b == 0:
        print(0)
    elif a * b < 10:
        print(a * b)
    elif a * b > 10:
        print(str(a) * b)
