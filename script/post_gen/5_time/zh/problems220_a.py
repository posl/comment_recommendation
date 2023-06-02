Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem220_a():
    a,b,c = map(int,input().split())
    for i in range(a,b+1):
        if i % c == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 2

def main():
    a,b,c = map(int,input().split())
    flag = 0
    for i in range(a,b+1):
        if i%c == 0:
            print(i)
            flag = 1
            break
    if flag == 0:
        print(-1)

=======
Suggestion 3

def main():
    a,b,c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 4

def main():
    A,B,C = map(int,input().split())
    if A % C == 0:
        print(A)
    else:
        print(-1)

=======
Suggestion 5

def main():
    A,B,C = map(int, input().split())
    for i in range(A,B+1):
        if i % C == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 6

def main():
    a,b,c = map(int, input().split())
    for i in range(a,b+1):
        if i % c == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 7

def solution():
    a,b,c = map(int,input().split())
    for i in range(a,b+1):
        if i%c == 0:
            print(i)
            break
    else:
        print(-1)

solution()
