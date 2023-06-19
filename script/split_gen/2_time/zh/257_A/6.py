def main():
    n, x = map(int, raw_input().split())
    if x % n == 0:
        print chr((x / n) + 64)
    else:
        print chr((x / n) + 65)
