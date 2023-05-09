Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b + 1):
        if i % c == 0:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            return
    print(-1)

main()

=======
Suggestion 4

def problems220_a():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    for i in range(a,b+1):
        if i%c == 0:
            print(i)
            exit()
    print(-1)

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    for i in range(a,b+1):
        if i % c == 0:
            print(i)
            exit()
    else:
        print(-1)

=======
Suggestion 7

def find_multiple(a, b, c):
    for i in range(a, b+1):
        if i % c == 0:
            return i
    return -1

=======
Suggestion 8

def main():
    A, B, C = map(int, input().split())
    #print(A, B, C)
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            return
    print(-1)
    return

main()

=======
Suggestion 9

def main():
    A, B, C = map(int, input().split())
    if A % C == 0:
        print(A)
    elif A % C != 0:
        print(A + (C - (A % C)))
    else:
        print(-1)
