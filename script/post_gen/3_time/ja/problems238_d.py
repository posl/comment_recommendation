Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    t = int(readline())
    for _ in range(t):
        a, s = map(int, readline().split())
        if a > s:
            print("No")
            continue
        elif a == s:
            print("Yes")
            continue
        else:
            if (s - a) & 1:
                print("No")
                continue
            else:
                print("Yes")
                continue

=======
Suggestion 2

def main():
    t = int(input())
    for i in range(t):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        if a == s:
            print("Yes")
            continue
        d = s - a
        if d % 2 == 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    t = int(input())
    for i in range(t):
        a,s = map(int,input().split())
        if a > s:
            print("No")
        elif a == s:
            print("Yes")
        else:
            if a & (s-a) == 0:
                print("Yes")
            else:
                print("No")

=======
Suggestion 4

def main():
    t = int(input())
    for i in range(t):
        a, s = map(int, input().split())
        if s < a:
            print("No")
        elif (s - a) % 2 == 1:
            print("No")
        else:
            print("Yes")

=======
Suggestion 5

def main():
    t = int(input())
    for i in range(t):
        a,s = map(int,input().split())
        if a > s:
            print("No")
            continue
        if a == s:
            print("Yes")
            continue
        if a == 0:
            print("No")
            continue
        if s % 2 == 0:
            if a % 2 == 0:
                print("Yes")
                continue
            else:
                print("No")
                continue
        else:
            if a % 2 == 1:
                print("Yes")
                continue
            else:
                print("No")
                continue

=======
Suggestion 6

def main():
    t = int(input())
    for i in range(t):
        a, s = map(int, input().split())
        if a > s:
            print('No')
        else:
            if a & (s - a) == 0:
                print('Yes')
            else:
                print('No')

=======
Suggestion 7

def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a > s:
            print('No')
        else:
            if a == s:
                print('Yes')
            else:
                if a == 0:
                    print('No')
                else:
                    if s % 2 == 0:
                        print('No')
                    else:
                        if a % 2 == 0:
                            print('No')
                        else:
                            print('Yes')

=======
Suggestion 8

def solve(a, s):
    if a > s:
        return False
    if s % 2 == 0 and a % 2 == 0:
        return True
    if s % 2 == 1 and a % 2 == 1:
        return True
    return False

=======
Suggestion 9

def main():
    T = int(input())
    for i in range(T):
        a,s = map(int, input().split())
        if s < a:
            print("No")
        else:
            if (s - a) % 2 == 0:
                print("Yes")
            else:
                print("No")

=======
Suggestion 10

def solve(a, s):
    if s < a:
        return False
    if s % 2 != a % 2:
        return False
    return True
