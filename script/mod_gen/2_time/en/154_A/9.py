def main():
    # Get input
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    # Check if U is S or T
    if U == S:
        A -= 1
    else:
        B -= 1
    # Print the answer
    print(A, B)

if __name__ == '__main__':
    main()