Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A,B,T=map(int,input().split())
    t=0
    for i in range(1,T+1):
        if i%A==0:
            t+=B
    print(t)

=======
Suggestion 2

def main():
    A,B,T=map(int,input().split())
    count=0
    for i in range(1,T+1):
        if i%A==0:
            count+=B
    print(count)

=======
Suggestion 3

def problems125_a():
    a,b,t = [int(i) for i in input().split()]
    count = 0
    for i in range(1,t+1):
        if i%a == 0:
            count += b
    print(count)

=======
Suggestion 4

def problem125_a():
    A, B, T = map(int, input().split())
    result = 0
    for i in range(T):
        if (i + 1) % A == 0:
            result += B
    print(result)

=======
Suggestion 5

def main():
    A,B,T = map(int,input().split())
    time = T + 0.5
    num = 0
    for i in range(1,time):
        if i % A == 0:
            num += B
    print(num)

=======
Suggestion 6

def main():
    a, b, t = map(int, input().split())
    count = 0
    for i in range(1, t+1):
        if i % a == 0:
            count += b
    print(count)

=======
Suggestion 7

def problem125_a():
    a,b,t = map(int,input().split())
    count = 0
    for i in range(1,t+1):
        if i%a == 0:
            count += b
    print(count)

=======
Suggestion 8

def problem125_a(a, b, t):
    count = 0
    for i in range(1, t + 1):
        if i % a == 0:
            count += 1
    return count * b

=======
Suggestion 9

def main():
    line = input()
    items = line.split()
    A = int(items[0])
    B = int(items[1])
    T = int(items[2])
    count = 0
    for i in range(1,T+1):
        if i % A == 0:
            count += B
    print(count)

=======
Suggestion 10

def main():
    a, b, t = map(int, input().split())
    print((t // a) * b)
