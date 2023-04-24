Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
        elif a == s:
            print("Yes")
        else:
            if (s - a) % 2 == 0:
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
            print('No')
        elif (s - a) % 2 == 1:
            print('No')
        else:
            print('Yes')

=======
Suggestion 3

def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
        elif a == s:
            print("Yes")
        elif (s - a) % 2 == 1:
            print("No")
        else:
            print("Yes")

=======
Suggestion 4

def main():
    T = int(input())
    for i in range(T):
        a,s = map(int,input().split())
        if a > s:
            print("No")
        elif (s-a)%2 == 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

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
Suggestion 6

def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        if a == s:
            print("Yes")
            continue
        if (s - a) % 2 == 0:
            print("Yes")
            continue
        print("No")

=======
Suggestion 7

def main():
    T = int(input())
    for _ in range(T):
        a,s = map(int,input().split())
        if a > s:
            print("No")
            continue
        if (s-a)%2 == 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    T = int(input())
    for _ in range(T):
        a,s = map(int,input().split())
        print("Yes" if a <= s and (s-a)%2 == 0 else "No")

=======
Suggestion 9

def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        ans = "No"
        if a <= s:
            if (s - a) % 2 == 0:
                ans = "Yes"
        print(ans)
