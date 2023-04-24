Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(a * d - b * c)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(a*d-b*c)

main()

=======
Suggestion 3

def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]
