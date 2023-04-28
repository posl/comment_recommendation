Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C, X = map(int, input().split())
    if X >= A:
        if X <= B:
            print((C/(B-A+1)))
        else:
            print(1)
    else:
        print(0)

=======
Suggestion 2

def main():
    A, B, C, X = map(int, input().split())
    if X <= A:
        print(1.0)
    elif A < X <= B:
        print(C / (B - A + 1))
    else:
        print(0.0)

main()

=======
Suggestion 3

def main():
    A, B, C, X = map(int, input().split())
    if X < A:
        print(0)
    elif X >= A and X <= B:
        print(1 / (B - A + 1))
    elif X > B and X <= B + C:
        print(C / (B - A + 1))
    else:
        print(0)

=======
Suggestion 4

def main():
    A, B, C, X = map(int, input().split())
    ans = 0
    if X >= A:
        ans += (B - A + 1)
        if X >= B:
            ans += (B - A + 1) * C
    print(ans / 1000)

=======
Suggestion 5

def main():
    A, B, C, X = map(int, input().split())
    print(1 - (B - X) / (B - A) if A <= X <= B else 0)

main()

=======
Suggestion 6

def main():
    A, B, C, X = map(int, input().split())

    if X <= A:
        ans = 1
    elif A < X <= B:
        ans = 1 - ((B - X + 1) / (B - A + 1)) * (C / (B - A + 1))
    else:
        ans = 0

    print(ans)

=======
Suggestion 7

def main():
    A, B, C, X = map(int, input().split())
    print((A <= X and X <= B) * C / (B - A + 1))

=======
Suggestion 8

def main():
    #input
    A,B,C,X = map(int, input().split())
    #output
    if X < A:
        print(0)
    elif A <= X <= B:
        print(1)
    else:
        print((C)/(B-A+1))

=======
Suggestion 9

def main():
    A, B, C, X = map(int, input().split())
    print((C/B) if A <= X <= B else 0)

=======
Suggestion 10

def main():
    A,B,C,X = map(int, input().split())
    print((min(B,X)-A+1)/B if A <= X <= B else 0)
