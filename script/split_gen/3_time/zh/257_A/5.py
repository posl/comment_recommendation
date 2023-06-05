def main():
    n, x = map(int, input().split())
    if x % n == 0:
        print(chr(x // n + 64))
    else:
        print(chr(x // n + 65))
