def main():
    N, A, B = map(int, input().split())
    print(A * (N // (A + B)) + min(A, N % (A + B)))

if __name__ == '__main__':
    main()