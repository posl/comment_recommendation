def main():
    a, b, k = map(int, input().split())
    if a >= b:
        print(0)
    else:
        print(max(0, min(b - a - 1, k)))
