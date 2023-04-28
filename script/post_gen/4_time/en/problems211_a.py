Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    C = ((A - B) / 3) + B
    print(C)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    C = ((A-B)/(3)) +B
    print(C)

=======
Suggestion 3

def meanArterialPressure(a, b):
    c = (a - b) / 3 + b
    return c

a, b = map(int, input().split())
print(meanArterialPressure(a, b))

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print((A-B)/3+B)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print((a - b)/3 + b)

=======
Suggestion 6

def main():
    # To read from STDIN
    import sys
    # To read from a file
    #import os
    #filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    #sys.stdin = open(filename, 'r')
    # To write to a file
    #filename = os.path.join(os.path.dirname(__file__), 'output.txt')
    #sys.stdout = open(filename, 'w')
    A, B = map(int, sys.stdin.readline().split())
    C = ((A-B)/(3)) +B
    print(C)
