def main():
    A, B, N = map(int, input().split())
    print(A * min(N, B-1) // B)

if __name__ == '__main__':
    main()