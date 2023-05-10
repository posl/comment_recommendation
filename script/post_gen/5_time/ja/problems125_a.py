Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, t = map(int, input().split())
    print(int(t//a)*b)

=======
Suggestion 2

def main():
    a, b, t = map(int, input().split())
    num = 0
    for i in range(1, t + 1):
        if i % a == 0:
            num += b
    print(num)

=======
Suggestion 3

def main():
    A, B, T = map(int, input().split())
    total = 0
    for i in range(1, T + 1):
        if i % A == 0:
            total += B
    print(total)
    return

=======
Suggestion 4

def main():
    a, b, t = map(int, input().split())
    count = 0
    for i in range(1, t + 1):
        if i % a == 0:
            count += b
    print(count)

=======
Suggestion 5

def main():
    a, b, t = map(int, input().split())
    print(b * (t // a))

=======
Suggestion 6

def main():
    A, B, T = map(int, input().split())
    print(int(T // A * B))
    return

=======
Suggestion 7

def main():
    A, B, T = map(int, input().split())
    print(B * (T // A))

=======
Suggestion 8

def main():
    # input
    A, B, T = map(int, input().split())

    # compute

    # output
    print((T//A)*B)

=======
Suggestion 9

def main():
    A, B, T = map(int, input().split())
    count = 0
    for i in range(1, T+1):
        if i % A == 0:
            count += B
    print(count)

=======
Suggestion 10

def solve():
    A,B,T = list(map(int,input().split()))
    ans = 0
    for i in range(1,T+1):
        if i%A == 0:
            ans += B
    print(ans)
