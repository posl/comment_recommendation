Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, T = map(int, input().split())
    count = 0
    for i in range(1, T + 1):
        if i % A == 0:
            count += B
    print(count)

=======
Suggestion 2

def main():
    a, b, t = map(int, input().split())
    ans = 0
    for i in range(1, t+1):
        if i % a == 0:
            ans += b
    print(ans)

=======
Suggestion 3

def main():
    a, b, t = map(int, input().split())
    cnt = 0
    for i in range(1, t + 1):
        if i % a == 0:
            cnt += b
    print(cnt)

=======
Suggestion 4

def main():
    a,b,t = map(int,input().split())
    i = 1
    j = 0
    while i <= t + 0.5:
        if i % a == 0:
            j += b
        i += 1
    print(j)

=======
Suggestion 5

def calc_biscuits(a, b, t):
    num = 0
    for i in range(1, t+1):
        if i % a == 0:
            num += b
    return num

=======
Suggestion 6

def biscuit_production():
    A, B, T = map(int, input().split())
    count = 0
    for i in range(T+1):
        if i % A == 0:
            count += B
    print(count)

=======
Suggestion 7

def main():
    A, B, T = map(int, input().split())
    print(int((T + 0.5)//A * B))

=======
Suggestion 8

def main():
    A, B, T = map(int, input().split())
    print(int(T // A * B))

=======
Suggestion 9

def main():
    a, b, t = map(int, input().split())
    print(int(t//a*b))

=======
Suggestion 10

def main():
    a, b, t = map(int, input().split())
    print(int(b * (t // a)))
