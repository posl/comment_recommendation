Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # input
    A1, A2, A3 = map(int, input().split())

    # compute

    # output
    print(min(abs(A1-A2)+abs(A2-A3), abs(A1-A3)+abs(A3-A2), abs(A2-A1)+abs(A1-A3)))

=======
Suggestion 2

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2] - A[0])

=======
Suggestion 3

def main():
    a = list(map(int, input().split()))
    a.sort()
    print(a[2] - a[0])

=======
Suggestion 4

def min_cost(tasks):
    return min(abs(tasks[0]-tasks[1])+abs(tasks[1]-tasks[2]), abs(tasks[0]-tasks[2])+abs(tasks[2]-tasks[1]), abs(tasks[0]-tasks[1])+abs(tasks[0]-tasks[2]))

=======
Suggestion 5

def main():
    # Get input here
    A_1, A_2, A_3 = map(int, input().strip().split())
    # Calculate result here
    result = 0
    if A_1 == A_2 == A_3:
        result = 0
    elif A_1 == A_2:
        result = abs(A_3 - A_1)
    elif A_1 == A_3:
        result = abs(A_2 - A_1)
    elif A_2 == A_3:
        result = abs(A_1 - A_2)
    else:
        result = min(abs(A_1 - A_2) + abs(A_2 - A_3), abs(A_1 - A_3) + abs(A_3 - A_2), abs(A_2 - A_1) + abs(A_1 - A_3))
    # Print result here
    print(result)

=======
Suggestion 6

def main():
    # input
    A = list(map(int, input().split()))
    # compute
    A.sort()
    # output
    print(A[2]-A[0])

=======
Suggestion 7

def main():
    a = list(map(int, input().split()))
    print(max(a)-min(a))
