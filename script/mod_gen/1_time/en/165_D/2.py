def main():
    A, B, N = map(int, input().split())
    if N < B:
        print(A * N // B - A * (N // B))
    else:
        print(A * (B - 1) // B - A * ((B - 1) // B))

if __name__ == '__main__':
    main()