Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, t = map(int, input().split())
    count = 0
    for i in range(1, t + 1):
        if i % a == 0:
            count += b
    print(count)

=======
Suggestion 2

def main():
    A, B, T = map(int, input().split())
    count = 0
    for i in range(1, T+1):
        if i % A == 0:
            count += B
    print(count)

=======
Suggestion 3

def main():
    A, B, T = map(int, input().split())
    print(B * (T // A))

=======
Suggestion 4

def main():
    a, b, t = map(int, input().split())
    print((t // a) * b)

=======
Suggestion 5

def main():
    a, b, t = map(int, input().split())
    print(b * (t // a))

=======
Suggestion 6

def main():
    A, B, T = map(int, input().split())
    print((T//A)*B)

=======
Suggestion 7

def main():
    line = input()
    a,b,t = line.split()
    a = int(a)
    b = int(b)
    t = int(t)

    count = 0
    for i in range(1, t+1):
        if i % a == 0:
            count += b
    print(count)

=======
Suggestion 8

def main():
    a, b, t = map(int, input().split())
    print(int((t+0.5)//a)*b)

=======
Suggestion 9

def main():
    a,b,t = map(int, input().split())
    print(int((t+0.5)/a)*b)

=======
Suggestion 10

def problems125_a():
    A, B, T = map(int, input().split())
    print((T//A)*B)
    return
