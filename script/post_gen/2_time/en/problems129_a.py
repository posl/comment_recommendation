Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    p, q, r = map(int, input().split())
    print(min(p + q, q + r, r + p))

=======
Suggestion 2

def main():
    P, Q, R = map(int, input().split())
    print(min(P+Q, Q+R, R+P))

=======
Suggestion 3

def main():
    P, Q, R = map(int, input().split())
    print(min(P + Q, P + R, Q + R))

main()

=======
Suggestion 4

def main():
    p,q,r = map(int,input().split())
    print(min(p+q,r+q,r+p))

=======
Suggestion 5

def main():
    # Get input
    P,Q,R = input().split()
    P = int(P)
    Q = int(Q)
    R = int(R)
    # Find the minimum of the sum of the flight times
    min = P + Q
    if min > P + R:
        min = P + R
    if min > Q + R:
        min = Q + R
    # Print the minimum of the sum of the flight times
    print(min)

=======
Suggestion 6

def min_flight_time():
    flight_time = list(map(int, input().split()))
    return sum(flight_time) - max(flight_time)

=======
Suggestion 7

def main():
    # Read data
    data = input()
    # Split data
    data = data.split(" ")
    # Convert to integers
    data = [int(i) for i in data]
    # Sort
    data.sort()
    # Print result
    print(data[0] + data[1])

=======
Suggestion 8

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
