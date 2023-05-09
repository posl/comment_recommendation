def main():
    n, x = map(int, input().split())
    x -= 1
    a = x // n
    b = x % n
    print(chr(a + ord('A') + b))
