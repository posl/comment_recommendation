Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def apple_pie(A, P):
    return 3*A + P

=======
Suggestion 2

def make_pie(apples, pieces):
    return (apples * 3 + pieces) // 2

print('请输入苹果的个数和苹果的块数，用空格分开')
apples, pieces = map(int, input().split())
print(make_pie(apples, pieces))

=======
Suggestion 3

def make_pie(apple, piece):
    if apple == 0:
        return 0
    elif piece == 1:
        return apple
    else:
        return apple // 2 + make_pie(apple - apple // 2 * 2, piece - 1)

=======
Suggestion 4

def make_pie(a, p):
    return (a * 3 + p) // 2

=======
Suggestion 5

def main():
    a, p = map(int, input().split())
    print((a * 3 + p) // 2)

=======
Suggestion 6

def max_pai(a,p):
    return (a*3+p)//2

=======
Suggestion 7

def max_pie(a, p):
    return (a * 3 + p) // 2

a, p = map(int, input().split())

print(max_pie(a, p))

=======
Suggestion 8

def solve(A, P):
    return (A * 3 + P) // 2

=======
Suggestion 9

def solve(a, p):
    return (a * 3 + p) // 2
