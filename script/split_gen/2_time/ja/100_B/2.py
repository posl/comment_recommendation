def main():
    d, n = map(int, input().split())
    if d == 0:
        print(n)
    elif d == 1:
        print(n * 100)
    else:
        print(n * 10000)
