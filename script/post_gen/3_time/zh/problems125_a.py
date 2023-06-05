Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(a, b, t):
    result = 0
    for i in range(1, t+1):
        if i % a == 0:
            result += b
    return result

=======
Suggestion 2

def main():
    A,B,T = map(int,input().split())
    count = 0
    for i in range(1,T+1):
        if i%A == 0:
            count += B
    print(count)

main()

=======
Suggestion 3

def main():
    A,B,T = map(int,input().split())
    count = 0
    for i in range(1,T+1):
        if i % A == 0:
            count = count + B
    print(count)

=======
Suggestion 4

def main():
    a, b, t = map(int, input().split())
    count = 0
    for i in range(1, t+1):
        if i % a == 0:
            count += b
    print(count)

=======
Suggestion 5

def main():
    A, B, T = map(int, input().split())
    count = 0
    for i in range(1, T+1):
        if i % A == 0:
            count += B
    print(count)

=======
Suggestion 6

def problem125_a():
    A,B,T = map(int, input().split())
    count = 0
    for i in range(T+1):
        if i%A == 0:
            count += B
    print(count)

=======
Suggestion 7

def main():
    a, b, t = map(int, input().split())
    print(int(t/a*b))

=======
Suggestion 8

def problem125_a():
    a, b, t = map(int, input().split())
    count = 0
    for i in range(1, t+1):
        if i % a == 0:
            count += b
    print(count)

=======
Suggestion 9

def problems125_a():
    A, B, T = map(int, input().split())
    print(int(T/A)*B)

problems125_a()
