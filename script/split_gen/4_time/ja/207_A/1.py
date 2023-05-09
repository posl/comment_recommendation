def main():
    a, b, c = map(int, input().split())
    if a == b and b == c:
        print(a * 3)
    else:
        print(max(a, b, c) * 2)
