def main():
    x = input()
    m = int(input())
    d = int(max(x))
    n = d + 1
    while int(x, n) <= m:
        n += 1
    print(n - d - 1)
