Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, T = [int(x) for x in input().split()]
    count = 0
    for i in range(1, T + 1):
        if i % A == 0:
            count += B
    print(count)

=======
Suggestion 2

def main():
    A, B, T = map(int, input().split())
    print(B * (T // A))

=======
Suggestion 3

def main():
    a, b, t = map(int, input().split())
    print((t // a) * b)

=======
Suggestion 4

def main():
    A, B, T = list(map(int, input().split()))
    print(B * (T // A))

=======
Suggestion 5

def main():
    A, B, T = map(int, input().split())
    print(sum([B for i in range(1, T//A + 2) if A*i <= T + 0.5]))

=======
Suggestion 6

def main():
    A, B, T = [int(i) for i in input().split()]
    print(int(T/A)*B)
