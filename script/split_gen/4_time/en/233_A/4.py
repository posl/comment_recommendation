def main():
    x, y = map(int, input().split())
    print((y - x) if y - x >= 0 else 0)
