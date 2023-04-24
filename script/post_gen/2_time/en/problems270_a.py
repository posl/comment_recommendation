Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    print(A + B - max(A, B))

=======
Suggestion 2

def main():
    A, B = input().split()
    A = int(A)
    B = int(B)
    C = A + B
    print(C)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print(A + B - min(A, B))

=======
Suggestion 4

def main():
    A, B = [int(x) for x in input().split()]
    print(A + B - (A & B))

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print(A + B - (A & B))

=======
Suggestion 6

def main():
    A,B = [int(i) for i in input().split()]
    print(A+B-max(A,B)+min(A,B))

=======
Suggestion 7

def main():
    # Read the input
    A,B = map(int,input().split())
    # Calculate the answer
    ans = 7 - A - B
    # Print the answer
    print(ans)
