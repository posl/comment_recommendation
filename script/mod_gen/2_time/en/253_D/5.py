def main():
    N, A, B = map(int, input().split())
    print(sum(range(1, N + 1)) - sum(range(A, N + 1, A)) - sum(range(B, N + 1, B)) + sum(range(A * B, N + 1, A * B)))

if __name__ == '__main__':
    main()