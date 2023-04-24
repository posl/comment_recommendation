Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(a * d - b * c)

=======
Suggestion 2

def determinant(a, b, c, d):
    return a * d - b * c

a, b = map(int, input().split())
c, d = map(int, input().split())
print(determinant(a, b, c, d))

=======
Suggestion 3

def main():
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(a[0]*b[1]-a[1]*b[0])

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    print(a*d-b*c)

main()

=======
Suggestion 5

def main():
    a, b = (int(x) for x in input().split())
    c, d = (int(x) for x in input().split())
    print(a*d-c*b)

=======
Suggestion 6

def solve(a, b, c, d):
    return a * d - b * c
