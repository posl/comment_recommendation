Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    P, Q, R = map(int, input().split())
    print(min(P + Q, Q + R, R + P))

=======
Suggestion 2

def main():
    P,Q,R = map(int,input().split())
    print(min(P+Q,P+R,Q+R))

=======
Suggestion 3

def main():
    p,q,r = map(int,input().split())
    print(min(p+q,p+r,q+r))

=======
Suggestion 4

def main():
    # Get the input
    P, Q, R = map(int, input().split())
    # Find the minimum of the sum of the flight times
    minSum = min(P + Q, Q + R, R + P)
    # Print the minimum of the sum of the flight times
    print(minSum)

main()
