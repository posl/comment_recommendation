def main():
    A, B = map(int, input().split())
    if B <= 2 * A:
        print(2 * A - B)
    else:
        print(0)
