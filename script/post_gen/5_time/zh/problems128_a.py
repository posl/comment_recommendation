Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def apple_pie(A, P):
    return (A * 3 + P) // 2

=======
Suggestion 2

def main():
    (A, P) = map(int, input().split())
    print((A * 3 + P) // 2)

=======
Suggestion 3

def main():
    A, P = map(int, input().split())
    print((A * 3 + P) // 2)

=======
Suggestion 4

def m():
    a, p = map(int, input().split())
    return (a * 3 + p) // 2


print(m())

=======
Suggestion 5

def apple_pie(a,p):
    return (3*a+p)//2

a,p = map(int,input().split())
print(apple_pie(a,p))

=======
Suggestion 6

def solve(A, P):
    return (A * 3 + P) // 2

=======
Suggestion 7

def main():
    a,p = input().split()
    a = int(a)
    p = int(p)
    print((a*3+p)//2)

=======
Suggestion 8

def problems128_a():
    a, p = map(int, input().split())
    print((a * 3 + p) // 2)

=======
Suggestion 9

def make_pie(apple, piece):
    if apple == 0:
        return 0
    else:
        return int(apple / 2) * 3 + (apple % 2) + int(piece / 2) * 3 + (piece % 2)
    
apple, piece = input().split()
apple = int(apple)
piece = int(piece)
print(make_pie(apple, piece))
