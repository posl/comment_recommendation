Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 2

def main():
    a,b,c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    if a%c == 0:
        print(a)
    else:
        for i in range(a+1,b+1):
            if i%c == 0:
                print(i)
                break
            elif i == b:
                print(-1)
main()

=======
Suggestion 4

def problem220_a():
    a,b,c = map(int,input().split())
    for i in range(a,b+1):
        if i%c == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 6

def f(a, b, c):
    result = -1
    for i in range(a, b+1):
        if i % c == 0:
            result = i
            break
    return result

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            exit()
    print(-1)

=======
Suggestion 8

def main():
    a,b,c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            break
    else:
        print(-1)
