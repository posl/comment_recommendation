def main():
    N, A, B = map(int, input().split())
    x = N // (A + B)
    y = N % (A + B)
    print(x * A + min(y, A))

if __name__ == '__main__':
    main()