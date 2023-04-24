Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(max(a + b, a - b, a * b))

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(max(A + B, A - B, A * B))

=======
Suggestion 3

def main():
    A, B = [int(x) for x in input().split()]
    print(max(A+B, A-B, A*B))

=======
Suggestion 4

def main():
    #Get the input
    A, B = map(int, input().split())
    #Print the largest number among A + B, A - B, and A × B.
    print(max(A + B, A - B, A * B))
