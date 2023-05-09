def main():
    # Read the input data
    P, Q, R = map(int, input().split())
    # Calculate the shortest route
    shortest_route = P + Q
    if Q + R < shortest_route:
        shortest_route = Q + R
    if R + P < shortest_route:
        shortest_route = R + P
    # Print the result
    print(shortest_route)

if __name__ == '__main__':
    main()