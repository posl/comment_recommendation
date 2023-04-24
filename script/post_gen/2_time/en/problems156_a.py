Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, R = map(int, input().split())
    if N >= 10:
        print(R)
    else:
        print(R + 100 * (10 - N))

=======
Suggestion 2

def main():
    N, R = map(int, input().split())
    if N >= 10:
        print(R)
    else:
        print(R + (100 * (10 - N)))

=======
Suggestion 3

def main():
    n, r = map(int, input().split())
    if n >= 10:
        print(r)
    else:
        print(r + (100 * (10 - n)))

=======
Suggestion 4

def main():
    n, r = map(int, input().split())
    if n < 10:
        print(r + 100 * (10 - n))
    else:
        print(r)

=======
Suggestion 5

def main():
    n, r = [int(x) for x in input().split()]
    if n >= 10:
        print(r)
    else:
        print(r + (100 * (10 - n)))

=======
Suggestion 6

def main():
    N, R = map(int, input().split())
    if N < 10:
        R += 100 * (10 - N)
    print(R)

=======
Suggestion 7

def main():
    n, r = map(int, input().split())
    print(r + (100 * (10 - n)) if n < 10 else r)

=======
Suggestion 8

def main():
    N, R = map(int, input().split())
    print(R + (100 * (10 - N)))

=======
Suggestion 9

def main():
    # Get input
    N, R = map(int, input().split())
    # Calculate Inner Rating
    IR = R + 100 * (10 - N)
    # Print Inner Rating
    print(IR)
