def main():
    # Input
    N, A, B = map(int, input().split())
    # Output
    print(min(N*A, B))

if __name__ == '__main__':
    main()