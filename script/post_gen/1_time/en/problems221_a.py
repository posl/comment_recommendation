Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(32 ** (a - b))

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(32 ** (A - B))

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print(32**(A-B))

main()

=======
Suggestion 4

def earthquake():
    a,b = map(int,input().split())
    return 32**(a-b)

print(earthquake())

=======
Suggestion 5

def magnitude():
    a,b=map(int,input().split())
    print(32**(a-b))
magnitude()

=======
Suggestion 6

def main():
    from builtins import int, map, list, print
    from sys import stdin, stdout

    # Read data
    a, b = map(int, stdin.readline().split())

    # Compute and print result
    result = 32**(a-b)
    stdout.write(str(result))

=======
Suggestion 7

def earthquake(A, B):
    return 32**(A-B)
