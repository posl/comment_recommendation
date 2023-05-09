def main():
    # Get the input
    input = raw_input().split(" ")
    N = int(input[0])
    A = int(input[1])
    X = int(input[2])
    Y = int(input[3])
    if N <= A:
        print N*X
    else:
        print A*X + (N-A)*Y

if __name__ == '__main__':
    main()