def main():
    # Read from stdin
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Calculate the total number of votes
    total_votes = sum(A)
    # Sort the votes
    A.sort(reverse=True)
    # Check if the M-th popular item has more than (1/(4M)) of the total number of votes
    if A[M-1] >= (total_votes / (4 * M)):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()