def main():
    a, b, c = map(int, input().split())
    if a >= b + c:
        print(0)
    else:
        print(b + c - a)
