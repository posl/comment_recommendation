def main():
    A, B, C, X = map(int, input().split())
    print((A <= X <= B) * (C / (B - A + 1)))
main()
