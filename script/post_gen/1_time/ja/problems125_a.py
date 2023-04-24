Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, t = map(int, input().split())
    ans = 0
    for i in range(1, t + 1):
        if i % a == 0:
            ans += b
    print(ans)

=======
Suggestion 2

def main():
    A, B, T = map(int, input().split())
    ans = 0
    for i in range(1, T + 1):
        if i % A == 0:
            ans += B
    print(ans)

=======
Suggestion 3

def main():
    A, B, T = map(int, input().split())
    count = 0
    for i in range(1, T + 1):
        if i % A == 0:
            count += B
    print(count)

=======
Suggestion 4

def main():
    a,b,t = map(int,input().split())
    count = 0
    for i in range(1,t+1):
        if i%a == 0:
            count += b
    print(count)

=======
Suggestion 5

def main():
    A, B, T = map(int, input().split())
    print((T // A) * B)

=======
Suggestion 6

def main():
    a, b, t = map(int, input().split())
    print((t//a)*b)

=======
Suggestion 7

def main():
    a,b,t = map(int,input().split())
    print(b*int(t/a))
