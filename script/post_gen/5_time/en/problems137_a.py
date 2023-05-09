Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    if a+b >= a-b and a+b >= a*b:
        print(a+b)
    elif a-b >= a+b and a-b >= a*b:
        print(a-b)
    elif a*b >= a+b and a*b >= a-b:
        print(a*b)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print(max(a+b, a-b, a*b))

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print(max([A+B, A-B, A*B]))

=======
Suggestion 4

def main():
    A,B = map(int,input().split())
    print(max(A+B,A-B,A*B))

=======
Suggestion 5

def largest_number():
    a, b = map(int, input().split())
    print(max(a+b, a-b, a*b))
