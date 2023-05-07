def main():
    # Read the input
    A, B, C = map(int, input().split())
    # Print the result
    print(max(A+B+C, A+B*C, A*B+C, A*B*C))

if __name__ == '__main__':
    main()