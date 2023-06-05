def main():
    A, B = map(int, input().split())
    print(1 + (A - 1) * B / (A ** 2 + 1) ** 0.5)
