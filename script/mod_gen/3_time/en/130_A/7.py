def main():
    # Get input
    X, A = map(int, input().split())
    # Print output
    print(0 if X < A else 10)

if __name__ == '__main__':
    main()