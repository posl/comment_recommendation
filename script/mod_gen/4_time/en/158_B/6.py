def main():
    N, A, B = map(int, input().split())
    n = N // (A + B)
    m = N % (A + B)
    print(n * A + min(m, A))

if __name__ == '__main__':
    main()