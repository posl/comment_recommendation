Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(A,P):
    return (A*3+P)//2

=======
Suggestion 2

def main():
    apple, piece = map(int, input().split())
    print(apple * 3 + piece)

=======
Suggestion 3

def solve(A, P):
    return int((A * 3 + P) / 2)

=======
Suggestion 4

def solve():
    A, P = map(int, input().split())
    print((A*3+P)//2)

=======
Suggestion 5

def apple_pie(a,p):
    return int((3*a+p)/2)

=======
Suggestion 6

def main():
    a,p = map(int,input().split())
    print((a*3+p)//2)

=======
Suggestion 7

def get_max_pie_count(apple_count, piece_count):
    if apple_count == 0 or piece_count == 0:
        return 0
    if apple_count == 1 and piece_count == 1:
        return 1
    if apple_count == 1 and piece_count == 2:
        return 1
    if apple_count == 1 and piece_count == 3:
        return 1
    if apple_count == 2 and piece_count == 1:
        return 2
    if apple_count == 2 and piece_count == 2:
        return 3
    if apple_count == 2 and piece_count == 3:
        return 3
    if apple_count == 3 and piece_count == 1:
        return 3
    if apple_count == 3 and piece_count == 2:
        return 4
    if apple_count == 3 and piece_count == 3:
        return 5
    if apple_count > 3 and piece_count > 3:
        piece_count = piece_count - 3
        return get_max_pie_count(apple_count, piece_count) + 1
    if apple_count > 3 and piece_count <= 3:
        return apple_count + piece_count - 2

=======
Suggestion 8

def main():
    A, P = map(int, input().split())
    print((A*3+P)//2)
