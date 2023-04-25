Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print((N + min(A, B, C, D, E) - 1) // min(A, B, C, D, E) + 4)

=======
Suggestion 2

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print((N-1)//min(A,B,C,D,E)+5)

=======
Suggestion 3

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print((N-1)//min(A, B, C, D, E) + 5)

main()

=======
Suggestion 4

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_time = min(A, B, C, D, E)
    print(-(-N // min_time) + 4)

=======
Suggestion 5

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_time = min(A, B, C, D, E)
    print((N + min_time - 1) // min_time + 4)

=======
Suggestion 6

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_value = min(A, B, C, D, E)
    print((N + min_value - 1) // min_value + 4)

=======
Suggestion 7

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_value = min(A, B, C, D, E)
    print(-(-N // min_value) + 4)

=======
Suggestion 8

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print((n + min(a, b, c, d, e) - 1) // min(a, b, c, d, e) + 4)
