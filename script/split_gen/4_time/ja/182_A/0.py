def main():
    a, b = map(int, input().split())
    if b >= 2 * a + 100:
        print(0)
    else:
        print(2 * a + 100 - b)
