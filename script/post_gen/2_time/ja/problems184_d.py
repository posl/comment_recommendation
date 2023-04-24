Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    print(A * B / (A + B) + B * C / (B + C) + C * A / (C + A))

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print(100 * a / (a+b+c) + 100 * b / (a+b+c) + 100 * c / (a+b+c) - 3)

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    print(2*A*B + 2*B*C + 2*C*A + A + B + C)

main()

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(A * B + B * C + C * A + A + B + C)

=======
Suggestion 5

def main():
    A, B, C = map(int, input().split())
    print(100 + (A-1) + (B-1) + (C-1))

=======
Suggestion 6

def main():
    A,B,C = map(int,input().split())
    #A,B,C = map(int,input().split())
    #A,B,C = map(int,input().split())
    #A,B,C = map(int,input().split())
    print(100)
    return

=======
Suggestion 7

def main():
    A, B, C = map(int, input().split())
    print(A/100 + B/100 + C/100)

=======
Suggestion 8

def main():
    A, B, C = map(int, input().split())
    ans = 0
    for i in range(100):
        ans += i * (A + B + C) * (A + B + C - 1) / (100 - i) / 100
        A, B, C = B, C, A
    print(ans)

=======
Suggestion 9

def main():
    A,B,C = map(int,input().split())
    print(A*(B+C)+B*C)

=======
Suggestion 10

def main():
    a,b,c = map(int,input().split())
    print(a*b*c/(a+b+c)/(a+b+c-1))
