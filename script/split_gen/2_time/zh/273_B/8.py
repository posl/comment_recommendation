def main():
    a, b = map(int, input().split())
    print((a + (10 ** b - a % (10 ** b)) % (10 ** b)) % (10 ** b))
