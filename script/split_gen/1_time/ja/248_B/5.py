def main():
    A, B, K = map(int, input().split())
    if B - A <= 2 * K:
        print(0)
    else:
        print(B - A - 2 * K)
main()
