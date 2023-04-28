Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 4

def main():
    A,B,C = map(int,input().split())
    for i in range(A,B+1):
        if i % C == 0:
            print(i)
            break
        elif i == B:
            print(-1)

=======
Suggestion 5

def main():
    inp = input().split()
    a = int(inp[0])
    b = int(inp[1])
    c = int(inp[2])
    for i in range(a, b + 1):
        if i % c == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 6

def main():
    A,B,C = list(map(int, input().split()))
    if A%C == 0:
        print(A)
    else:
        for i in range(A+1,B+1):
            if i%C == 0:
                print(i)
                break
        else:
            print(-1)

=======
Suggestion 7

def main():
    a,b,c = map(int, input().split())
    if a%c == 0:
        print(a)
    else:
        print(((a//c)+1)*c if a//c < b//c else -1)
