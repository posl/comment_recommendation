def main():
    a, b, c, d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print("Yes")
