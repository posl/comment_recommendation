def main():
    d, n = map(int, input().split())
    if n != 100:
        print(100**d * n)
    else:
        print(100**d * n + 100**d)
