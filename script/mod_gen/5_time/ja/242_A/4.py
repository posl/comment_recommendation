def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1.0)
    elif X >= B:
        print(0.0)
    else:
        print((B - X) / (B - A))

if __name__ == '__main__':
    main()