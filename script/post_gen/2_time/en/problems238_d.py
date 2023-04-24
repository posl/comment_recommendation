Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        if a == s:
            print("Yes")
        elif a > s:
            print("No")
        else:
            if (s - a) % 2 == 0:
                print("Yes")
            else:
                print("No")

=======
Suggestion 2

def main():
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        if a > s:
            print('No')
        elif a == s:
            print('Yes')
        else:
            if a % 2 == s % 2:
                print('Yes')
            else:
                print('No')

main()

=======
Suggestion 3

def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a == 0 and s == 0:
            print("Yes")
        elif a == 0:
            print("No")
        elif a > s:
            print("No")
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
    for _ in range(T):
        a,s = map(int,input().split())
        if a > s:
            print('No')
        elif a == s:
            print('Yes')
        elif a*2 > s:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def solve():
    a,s=map(int,input().split())
    if a>s:
        print("No")
        return
    if (s-a)%2==0:
        print("Yes")
    else:
        print("No")
    return

=======
Suggestion 7

def solve(a,s):
    if a == 0:
        if s == 0:
            return "Yes"
        else:
            return "No"
    if s < a:
        return "No"
    if s % 2 == 0 and a % 2 == 0:
        return "Yes"
    if s % 2 == 1 and a % 2 == 1:
        return "Yes"
    return "No"
T = int(input())
for _ in range(T):
    a,s = map(int,input().split())
    print(solve(a,s))

=======
Suggestion 8

def solve(a, s):
    if a > s:
        return False
    elif a == s:
        return True
    elif s % 2 == 0:
        return True
    else:
        return False

=======
Suggestion 9

def isYes(a, s):
    if a == 0:
        if s == 0:
            return "Yes"
        else:
            return "No"
    if s < a:
        return "No"
    if s % 2 == 0:
        return "Yes"
    else:
        return "No"
