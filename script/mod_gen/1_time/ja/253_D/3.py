def main():
    N, A, B = map(int, input().split())
    print(N - (N // A + N // B - N // (A * B)))

if __name__ == '__main__':
    main()