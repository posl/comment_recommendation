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
    print((N-1)//min(A,B,C,D,E)+5)

=======
Suggestion 2

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(5 + (N - 1) // min(A, B, C, D, E))

=======
Suggestion 3

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    min_people = min(A,B,C,D,E)
    min_time = N // min_people
    if N % min_people != 0:
        min_time += 1
    min_time += 4
    print(min_time)

=======
Suggestion 4

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    #print(N, A, B, C, D, E)

    #print(N//min(A,B,C,D,E) + 5)

    print(int(5 + (N-1)//min(A,B,C,D,E)))

=======
Suggestion 5

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(5 + (n-1)//min(a,b,c,d,e))
    return 0

=======
Suggestion 6

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(int((N-1)//min(A,B,C,D,E)) + 5)

=======
Suggestion 7

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(4 + (n-1)//min(a,b,c,d,e))

=======
Suggestion 8

def main():
    N,A,B,C,D,E = map(int, input().split())
    print((N-1)//min(A,B,C,D,E)+5)

=======
Suggestion 9

def calc_min_time(n, a, b, c, d, e):
    # n people
    # a train
    # b bus
    # c taxi
    # d airplane
    # e ship
    return int(5 + (n-1)//min(a,b,c,d,e))
