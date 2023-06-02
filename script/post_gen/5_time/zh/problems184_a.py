Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c,d = map(int,input().split())
    print(a*d-b*c)

=======
Suggestion 2

def main():
    A = []
    for i in range(2):
        A.append([int(i) for i in input().split()])
    print(A[0][0]*A[1][1]-A[0][1]*A[1][0])

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(a*d-b*c)
