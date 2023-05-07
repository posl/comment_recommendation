def main():
    N = int(input())
    # N = A * B + C
    # A * B = N - C
    # A = (N - C) / B
    # A = (N - C) // B
    # A * B = (N - C) // B * B
    # A * B = N - C - (N - C) % B
    # A * B = C + (N - C) % B
    # C = A * B - (N - C) % B
    # C = A * B - N % B
    # C = A * B - (N - (N // B) * B)
    # C = A * B - (N - N + N

if __name__ == '__main__':
    main()