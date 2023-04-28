Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(max(0, a - 2 * b))

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(max(0, A - 2 * B))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a - 2*b < 0:
        print(0)
    else:
        print(a - 2*b)

=======
Suggestion 4

def main():
    input = raw_input().rstrip().split()
    a = int(input[0])
    b = int(input[1])
    if a <= b:
        print 0
    else:
        print a - b * 2

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    if a > b:
        print(0)
    else:
        print(b-a*2)

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    ans = max(0, A - 2 * B)
    print(ans)

=======
Suggestion 7

def main():
    # Take input Here and Call solution function
    A,B = map(int,input().strip().split())
    print(solution(A,B))

=======
Suggestion 8

def main():
    A = int(input())
    B = int(input())
    print(max(0, A - 2 * B))
    return

=======
Suggestion 9

def main():
    # Take input from user
    A, B = map(int, input().split())
    # Calculate the uncovered part of the window
    uncovered = A - (2 * B)
    # Check if the uncovered part is less than or equal to zero
    if uncovered <= 0:
        # Print zero
        print(0)
    else:
        # Print the uncovered part
        print(uncovered)
