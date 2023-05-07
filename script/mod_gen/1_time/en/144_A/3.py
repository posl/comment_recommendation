def main():
    # Read the numbers from the input
    A, B = map(int, input().split())
    # Check if the numbers are between 1 and 9
    if A < 1 or A > 20 or B < 1 or B > 20:
        print(-1)
    else:
        print(A * B)

if __name__ == '__main__':
    main()