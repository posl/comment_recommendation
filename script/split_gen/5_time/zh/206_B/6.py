def main():
    n = int(input())
    x = 0
    while x * (x + 1) / 2 < n:
        x += 1
    print(x)
