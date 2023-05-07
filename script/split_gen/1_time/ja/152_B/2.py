def main():
    a, b = map(int, input().split())
    if a * b > 0:
        print(min(str(a) * b, str(b) * a))
    else:
        print(max(str(a) * b, str(b) * a))
