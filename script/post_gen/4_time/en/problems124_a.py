Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    print(max(A + A - 1, B + B - 1, A + B))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(max(a + a - 1, a + b, b + b - 1))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(max(a + b, a + a - 1, b + b - 1))

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print(max(A*2-1, B*2-1, A+B))

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if A == B:
        print(A + B)
    else:
        print(max(A, B) * 2 - 1)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(max(a+b, a+a-1, b+b-1))

main()

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if a == b:
        print(a*2)
    else:
        print(max(a, b)*2-1)

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    print(max(a+a-1,b+b-1,a+b))
