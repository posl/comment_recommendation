Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(max(a, b, c) - min(a, b, c))

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])

=======
Suggestion 3

def find_min_cost(a1, a2, a3):
    cost1 = abs(a2-a1) + abs(a3-a2)
    cost2 = abs(a3-a1) + abs(a2-a3)
    cost3 = abs(a1-a2) + abs(a3-a1)
    return min(cost1, cost2, cost3)

=======
Suggestion 4

def main():
    A = list(map(int,input().split()))
    A.sort()
    print(A[2]-A[0])

=======
Suggestion 5

def main():
    # Get input here
    a1, a2, a3 = map(int, input().split())
    # Calculate result here
    print(min(abs(a1 - a2) + abs(a2 - a3), abs(a1 - a3) + abs(a3 - a2), abs(a2 - a1) + abs(a1 - a3)))
    # Print output here

=======
Suggestion 6

def main():
    # Get input here
    A = list(map(int, input().strip().split()))
    # Calculate result here
    A.sort()
    print(A[2] - A[0])
    # Print result here

main()

=======
Suggestion 7

def main():
    a = list(map(int, input().split()))
    print(max(a) - min(a))

=======
Suggestion 8

def main():
    # Get input here
    A = [int(x) for x in input().strip().split()]
    # Calculate result here
    A.sort()
    print(A[2]-A[0])
