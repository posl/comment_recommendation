def main():
    n, x = map(int, input().split())
    print(chr(64 + int((x - 1) / n + 1)))
