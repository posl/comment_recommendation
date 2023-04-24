Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, T = map(int, input().split())
    count = 0
    for i in range(1, T + 1):
        if i % A == 0:
            count += B
    print(count)

=======
Suggestion 2

def main():
    A, B, T = [int(x) for x in input().split()]
    total = 0
    for i in range(1, T + 1):
        if i % A == 0:
            total += B
    print(total)

=======
Suggestion 3

def main():
    a, b, t = map(int, input().split())
    print(b * (t // a))

=======
Suggestion 4

def main():
    A, B, T = map(int, input().split())
    print(B * (T // A))

=======
Suggestion 5

def main():
    a, b, t = map(int, input().split())
    print((t // a) * b)

=======
Suggestion 6

def main():
    # Read input
    A, B, T = map(int, input().split())

    # Compute answer
    answer = B * (T // A)

    # Print answer
    print(answer)
