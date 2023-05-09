def main():
    n, x = map(int, input().split())
    print(chr(64 + (x - 1) % 26))
