Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # T = int(input())
    T = 1
    for i in range(T):
        # a, s = map(int, input().split())
        a, s = 1, 8
        print("Yes" if s >= a and (s - a) % 2 == 0 else "No")

=======
Suggestion 2

def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        if s % 2 == 0:
            if a % 2 == 0:
                print("Yes")
            else:
                print("No")
        else:
            if a % 2 == 1:
                print("Yes")
            else:
                print("No")

=======
Suggestion 3

def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        if (s - a) & (2 * a - s) == 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    t = int(input())
    for i in range(t):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        if s - a < a:
            print("No")
            continue
        if s % 2 == 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        x = s - a
        if a & x:
            print("No")
        else:
            print("Yes")

=======
Suggestion 6

def main():
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        if a > s:
            print('No')
        else:
            if s % 2 == 1:
                if a % 2 == 1:
                    print('Yes')
                else:
                    print('No')
            else:
                if a % 2 == 0:
                    print('Yes')
                else:
                    print('No')

=======
Suggestion 7

def main():
    t = int(input())
    for i in range(t):
        a, s = map(int, input().split())
        if s < a:
            print('No')
        elif (s-a) % 2 == 1:
            print('No')
        else:
            print('Yes')

=======
Suggestion 8

def main():
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        if a == 0 and s == 0:
            print("Yes")
            continue
        if a == 0:
            print("No")
            continue
        if a & 1 == 1 and s & 1 == 0:
            print("No")
            continue
        if a & 1 == 0 and s & 1 == 1:
            print("No")
            continue
        if a & 1 == 1 and s & 1 == 1:
            print("Yes")
            continue
        if a & 1 == 0 and s & 1 == 0:
            print("Yes")
            continue

=======
Suggestion 9

def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        if (s - a) & 1 == 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    T = int(input())
    for i in range(T):
        a,s = map(int,input().split())
        if s < a:
            print('No')
        else:
            if (s-a)%2 == 0:
                print('Yes')
            else:
                print('No')
