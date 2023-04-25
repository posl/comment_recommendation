Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if S == U:
        A -= 1
    else:
        B -= 1
    print(A, B)

=======
Suggestion 2

def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    if s == u:
        a -= 1
    else:
        b -= 1
    print(a, b)

=======
Suggestion 3

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()

    if U == S:
        A -= 1
    else:
        B -= 1

    print(A, B)

=======
Suggestion 4

def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if U == S:
        print(A-1, B)
    else:
        print(A, B-1)

=======
Suggestion 5

def main():
    s,t = input().split()
    a,b = map(int,input().split())
    u = input()
    if s == u:
        a -= 1
    else:
        b -= 1
    print(a,b)
main()

=======
Suggestion 6

def main():
    # get input
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    # process
    if s == u:
        a -= 1
    else:
        b -= 1
    # output
    print(a, b)

=======
Suggestion 7

def main():
    #S = input()
    #T = input()
    #A, B = [int(x) for x in input().split()]
    #U = input()
    S = "red"
    T = "blue"
    A = 3
    B = 4
    U = "red"
    if S == U:
        A -= 1
    elif T == U:
        B -= 1
    print(A, B)
