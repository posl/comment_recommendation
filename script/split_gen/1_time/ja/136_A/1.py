def main():
    a, b, c = map(int, input().split())
    print(max(0, c - (a - b)))
