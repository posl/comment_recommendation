def main():
    # Get the number of queries
    Q = int(input())
    # Initialize the list
    S = []
    # Process the queries
    for i in range(Q):
        # Get the query
        query = input().split()
        # Process the query
        if query[0] == '1':
            # Get the integer
            x = int(query[1])
            # Add the integer to the list
            S.append(x)
        elif query[0] == '2':
            # Get the integer and the count
            x = int(query[1])
            c = int(query[2])
            # Remove the integer from the list c times
            for j in range(min(c, S.count(x))):
                S.remove(x)
        else:
            # Print the maximum value of the list minus the minimum value of the list
            print(max(S) - min(S))

if __name__ == '__main__':
    main()