def main():
    x, k = map(int, input().split())
    print(x + (10 ** k - x % (10 ** k)) % (10 ** k))
