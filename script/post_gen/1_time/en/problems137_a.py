Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    print(max(A + B, A - B, A * B))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(max(a+b, a-b, a*b))

=======
Suggestion 3

def main():
    a, b = [int(x) for x in input().split()]
    print(max(a+b, a-b, a*b))

=======
Suggestion 4

def read_input():
    return input().split()
