Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
        elif (s - a) % 2 == 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
        elif (s - a) % 2 == 1:
            print("No")
        else:
            print("Yes")

=======
Suggestion 3

def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if s < a:
            print("No")
        elif (s - a) % 2 == 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    T = int(input())
    for i in range(T):
        a,s = map(int,input().split())
        if a > s:
            print("No")
        elif a == s:
            print("Yes")
        else:
            if (s-a)%2 == 0:
                print("Yes")
            else:
                print("No")

=======
Suggestion 5

def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a == 0 and s == 0:
            print("Yes")
        elif a == 0 or s == 0:
            print("No")
        elif a > s:
            print("No")
        else:
            if (s - a) % 2 == 0:
                print("Yes")
            else:
                print("No")

=======
Suggestion 6

def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
        elif (a - s) % 2 == 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    for _ in range(int(input())):
        a,s = map(int,input().split())
        if a > s:
            print("No")
        elif (s-a)%2 == 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def solve():
    a, s = map(int, input().split())
    x = (s - a) // 2
    y = x + a
    if x >= 0 and x + y == s and x & y == a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def solve(a,s):
    if a > s:
        return "No"
    elif a == s:
        return "Yes"
    elif (s - a) % 2 == 0:
        return "Yes"
    else:
        return "No"

=======
Suggestion 10

def solve(a,s):
    if a>s:
        return "No"
    if a==s:
        if a==0:
            return "Yes"
        return "No"
    if (s-a)&1==1:
        return "No"
    return "Yes"
