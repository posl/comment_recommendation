Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(max(a+b, a-b, a*b))

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(max(A+B, A-B, A*B))

=======
Suggestion 3

def main():
    # Get input here
    a, b = map(int, input().strip().split())

    # Calculate result here
    result = max(a+b, a-b, a*b)

    # Print output here
    print(result)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    sum = a + b
    diff = a - b
    prod = a * b
    print(max(sum, diff, prod))
