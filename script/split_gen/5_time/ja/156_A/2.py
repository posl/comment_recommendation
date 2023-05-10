def main():
    n, r = map(int, input().split(' '))
    print(r + 100 * (10 - min(n, 10)))
