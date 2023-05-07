def main():
    # Read the data from the standard input
    A = map(int, raw_input().split())
    A.sort()
    # Check the condition
    if A[2] - A[1] == A[1] - A[0]:
        print "Yes"
    else:
        print "No"

if __name__ == '__main__':
    main()