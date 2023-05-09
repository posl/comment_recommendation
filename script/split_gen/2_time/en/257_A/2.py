def main():
    n, x = map(int, input().split())
    if x <= n:
        print(chr(64 + x))
    else:
        x -= n
        print(chr(64 + x // n + 1))
