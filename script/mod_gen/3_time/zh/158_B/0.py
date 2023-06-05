def main():
    N, A, B = map(int, input().split())
    if A > B:
        print(0)
    elif N == 1:
        if A == B:
            print(1)
        else:
            print(0)
    else:
        print((N - 2) * B + A - (N - 2) * A - B + 1)

if __name__ == '__main__':
    main()