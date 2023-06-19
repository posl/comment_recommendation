def main():
    a, b = map(int, input().split())
    if a <= b:
        print(b + max(b - 1, a))
    else:
        print(a + max(a - 1, b))
