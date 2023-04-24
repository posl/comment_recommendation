Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, r = map(int, input().split())
    if n >= 10:
        print(r)
    else:
        print(r + 100 * (10 - n))

main()

=======
Suggestion 2

def main():
    N, R = map(int, input().split())
    if N >= 10:
        print(R)
    else:
        print(R + 100 * (10 - N))

=======
Suggestion 3

def main():
    n, r = map(int, input().split())
    if n >= 10:
        print(r)
    else:
        print(r + 100 * (10 - n))

=======
Suggestion 4

def main():
    N, R = map(int, input().split())
    if N < 10:
        print(R + 100 * (10 - N))
    else:
        print(R)

=======
Suggestion 5

def main():
    N, R = map(int, input().split())
    if N >= 10:
        print(R)
    else:
        print(R + (100 * (10 - N)))

=======
Suggestion 6

def main():
    n, r = map(int, input().split())
    if n >= 10:
        print(r)
    else:
        print(r + (100 * (10 - n)))

=======
Suggestion 7

def main():
    N, R = map(int, input().split())
    if N < 10:
        R += 100 * (10 - N)
    print(R)
