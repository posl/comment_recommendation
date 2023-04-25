Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(a * d - b * c)

=======
Suggestion 2

def det(a, b, c, d):
    return (a * d) - (b * c)

a, b = [int(x) for x in input().split()]
c, d = [int(x) for x in input().split()]

print(det(a, b, c, d))

=======
Suggestion 3

def main():
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    print(a*d-b*c)
main()

=======
Suggestion 4

def read_matrix():
    matrix = []
    for i in range(2):
        matrix.append(list(map(int, input().split())))
    return matrix
