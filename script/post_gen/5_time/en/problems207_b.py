Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C, D = map(int, input().split())
    if A <= B * D:
        print(-1)
    else:
        print(-(-C // (A - B * D)))

=======
Suggestion 2

def solve(a, b, c, d):
    if a <= b * d:
        return -1
    else:
        return (a + b - c - 1) // (b - c)

=======
Suggestion 3

def main():
    a,b,c,d = map(int, input().split())
    if a <= b*d:
        print(-1)
    else:
        print((a+b-1)//b)

=======
Suggestion 4

def solve():
    a,b,c,d = map(int, input().split())
    if a <= b*d:
        print(-1)
    else:
        print((a+b*d-1)//(b*c-d))

=======
Suggestion 5

def main():
    A, B, C, D = map(int, input().split())
    if A <= B * D:
        print(-1)
        exit()
    else:
        for i in range(1, 10**5):
            if A <= (B * i) + (C * i * D):
                print(i)
                exit()

=======
Suggestion 6

def solve(A,B,C,D):
    if A <= B * D:
        return -1
    else:
        return (A + B - C - 1) // (B - C)

=======
Suggestion 7

def solve():
    A,B,C,D = map(int, input().split())
    if A <= B*D:
        print(-1)
        return
    if B >= C*D:
        print(-1)
        return
    if B >= A:
        print(1)
        return
    print((A-B-1)//(C*D-B)+1)

=======
Suggestion 8

def main():
    # input
    A, B, C, D = map(int, input().split())
    # compute
    if A > B * D:
        result = -1
    else:
        result = (C * A - 1) // (B * D - A) + 1
    # output
    print(result)

=======
Suggestion 9

def main():
    a,b,c,d = map(int, input().split())
    if a > b * c:
        print(-1)
        return
    if a <= b * c:
        if a % (b * d) == 0:
            print(a // (b * d))
            return
        else:
            print(a // (b * d) + 1)
            return

=======
Suggestion 10

def solve(a,b,c,d):
    ans = 0
    if b >= a:
        ans = 1
    else:
        if (a-b) % (b-c) == 0:
            ans = (a-b) // (b-c) + 1
        else:
            ans = (a-b) // (b-c) + 2
    return ans
