Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c = map(int,input().split())
    ans = 0
    ans += a/(a+b+c)
    ans += b/(a+b+c)
    ans += c/(a+b+c)
    print(100/ans-1)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print((a*b+b*c+c*a)/(a*b+b*c+c*a-a**2-b**2-c**2))

=======
Suggestion 3

def solve(A, B, C):
    # Write your code here
    return 0

A, B, C = map(int, input().split())
ans = solve(A, B, C)
print(ans)

=======
Suggestion 4

def main():
    a, b, c = [int(x) for x in input().strip().split()]
    print((a*(a+1) + b*(b+1) + c*(c+1))/2)

=======
Suggestion 5

def solve():
    A,B,C = map(int, input().split())
    ans = 0
    while A+B+C > 2:
        ans += 1
        if A > 0:
            A -= 1
            B += 1
        elif B > 0:
            B -= 1
            C += 1
        else:
            C -= 1
            A += 1
    print(ans + A/3 + B/3 + C/3)

=======
Suggestion 6

def main():
    a,b,c = map(int, input().split())
    print((a*b*c)/(a*b+b*c+c*a-a*a-b*b-c*c))

=======
Suggestion 7

def main():
    a,b,c = map(int, input().split())
    print((a*b*c)/(a*b+b*c+c*a))

=======
Suggestion 8

def main():
    input = sys.stdin.readline
    a, b, c = map(int, input().split())
    print((a*b*c)/((a*b)+(b*c)+(c*a)))

=======
Suggestion 9

def solve(a, b, c):
    return 0
