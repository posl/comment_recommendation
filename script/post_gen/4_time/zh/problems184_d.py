Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_expectation(a, b, c):
    if a + b + c == 0:
        return 0
    return (a * get_expectation(a - 1, b, c) + b * get_expectation(a + 1, b - 1, c) + c * get_expectation(a, b + 1, c - 1)) / (a + b + c) + 1

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print((a * (a + b + c) - a * a) / (a + b + c - a))

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def solve(a,b,c):
    if a==0 and b==0 and c==0:
        return 0
    return a/(a+b+c)*(solve(a+1,b-1,c)+1)+b/(a+b+c)*(solve(a,b+1,c-1)+1)+c/(a+b+c)*(solve(a,b,c+1)+1)

a,b,c=map(int,input().split())
print(solve(a,b,c))

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    if a == b == c:
        print(1)
    else:
        print((a*b*c)/(a*b+b*c+c*a))

=======
Suggestion 6

def get_expectation(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    total = a + b + c
    if a == 0:
        return total
    if b == 0:
        return total
    if c == 0:
        return total
    if a == 1:
        return total
    if b == 1:
        return total
    if c == 1:
        return total
    if a == 2:
        return total
    if b == 2:
        return total
    if c == 2:
        return total
    if a == 3:
        return total
    if b == 3:
        return total
    if c == 3:
        return total
    if a == 4:
        return total
    if b == 4:
        return total
    if c == 4:
        return total
    if a == 5:
        return total
    if b == 5:
        return total
    if c == 5:
        return total
    if a == 6:
        return total
    if b == 6:
        return total
    if c == 6:
        return total
    if a == 7:
        return total
    if b == 7:
        return total
    if c == 7:
        return total
    if a == 8:
        return total
    if b == 8:
        return total
    if c == 8:
        return total
    if a == 9:
        return total
    if b == 9:
        return total
    if c == 9:
        return total
    if a == 10:
        return total
    if b == 10:
        return total
    if c == 10:
        return total
    if a == 11:
        return total
    if b == 11:
        return total
    if c == 11:
        return total
    if a == 12:
        return total
    if b == 12:
        return total
    if c == 12:
        return total
    if a == 13:
        return total
    if b == 13:
        return total
    if c == 13:
        return total
    if

=======
Suggestion 7

def solve():
    A, B, C = map(int, input().split())
    print((A*B + B*C + C*A)/(A+B+C))
solve()

=======
Suggestion 8

def main():
    a, b, c = map(int, input().split())
    # a, b, c = 99, 99, 99
    # a, b, c = 98, 99, 99
    # a, b, c = 0, 0, 1
    # a, b, c = 31, 41, 59
    # a, b, c = 0, 0, 0
    # a, b, c = 1, 1, 1
    # a, b, c = 1, 0, 0
    # a, b, c = 0, 1, 0
    # a, b, c = 0, 0, 1
    # a, b, c = 1, 0, 1
    # a, b, c = 1, 1, 0
    # a, b, c = 0, 1, 1
    # a, b, c = 1, 1, 2
    # a, b, c = 1, 2, 1
    # a, b, c = 2, 1, 1
    # a, b, c = 1, 2, 2
    # a, b, c = 2, 1, 2
    # a, b, c = 2, 2, 1
    # a, b, c = 2, 2, 2
    # a, b, c = 2, 2, 3
    # a, b, c = 2, 3, 2
    # a, b, c = 3, 2, 2
    # a, b, c = 2, 3, 3
    # a, b, c = 3, 2, 3
    # a, b, c = 3, 3, 2
    # a, b, c = 3, 3, 3
    # a, b, c = 3, 3, 4
    # a, b, c = 3, 4, 3
    # a, b, c =

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    print((a*b*b+b*a*b)/(a*b+b*c+c*a))
