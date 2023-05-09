def main():
    N, A, B = map(int, input().split())
    x = N // A
    y = N // B
    z = N // (A * B)
    print(N * (x + y) - A * (x * (x + 1) // 2) - B * (y * (y + 1) // 2) + A * B * (z * (z + 1) // 2))

if __name__ == '__main__':
    main()