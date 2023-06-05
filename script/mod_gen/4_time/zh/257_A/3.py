def problems257_a():
    n, x = map(int, input().split())
    print(chr(x % 26 + 64))

if __name__ == '__main__':
    problems257_a()