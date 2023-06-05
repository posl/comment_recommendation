Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,t=map(int,input().split())
    sum=0
    for i in range(1,t+1):
        if i%a==0:
            sum+=b
    print(sum)

=======
Suggestion 2

def main():
    a,b,t = map(int, input().split())
    print(int(t/a)*b)

=======
Suggestion 3

def main():
    a, b, t = map(int, input().split())
    result = 0
    for i in range(1, t + 1):
        if i % a == 0:
            result += b
    print(result)

=======
Suggestion 4

def main():
    A,B,T = map(int,input().split())
    t = 1
    count = 0
    while t <= T + 0.5:
        if t % A == 0:
            count += B
        t += 1
    print(count)

=======
Suggestion 5

def main():
    A, B, T = map(int, input().split())
    count = 0
    for i in range(1, T + 1):
        if i % A == 0:
            count += B
    print(count)

=======
Suggestion 6

def problem125_a():
    pass

=======
Suggestion 7

def solve(a, b, t):
    cookie = 0
    for i in range(1, t+1):
        if i % a == 0:
            cookie += b
    return cookie

=======
Suggestion 8

def calNum(A,B,T):
    num = 0
    for i in range(1,T+1):
        if i%A == 0:
            num += B
    return num

=======
Suggestion 9

def cookie_maker():
    a, b, t = map(int, input().split())
    count = 0
    for i in range(1, t+1):
        if i % a == 0:
            count += b
    print(count)
    return 0

cookie_maker()
