def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1.0)
    elif A < X <= B:
        print(C / (B - A + 1))
    else:
        print(0.0)
main()
