Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a == s:
            print("Yes")
        elif a > s:
            print("No")
        elif a < s:
            if (s-a) % 2 == 0:
                print("Yes")
            else:
                print("No")

=======
Suggestion 2

def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
            continue
        if (s - a) % 2 == 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        if a > s:
            print('No')
        elif a == s:
            if a == 0:
                print('Yes')
            else:
                print('No')
        else:
            if (s - a) % 2 == 0:
                print('Yes')
            else:
                print('No')

=======
Suggestion 4

def solve(a, s):
    if a > s:
        return 'No'
    elif a == s:
        return 'Yes'
    elif (s - a) % 2 == 0:
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 5

def solve():
    a,s=map(int,input().split())
    if a==s:
        print("Yes")
        return
    if a>s:
        print("No")
        return
    if a==0:
        print("No")
        return
    if (s-a)&1==1:
        print("No")
        return
    print("Yes")
    return

=======
Suggestion 6

def solve():
    a,s = map(int,input().split())
    if a > s:
        print("No")
        return
    if a == s:
        if s == 0:
            print("Yes")
        else:
            print("No")
        return
    if (s-a)%2 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def solve(a, s):
    if a > s:
        return 'No'
    if a == s:
        return 'Yes'
    if s % 2 == 1:
        return 'No'
    x = s // 2
    if a < x:
        return 'No'
    return 'Yes'

=======
Suggestion 8

def check(a,s):
    if a==0:
        if s==0:
            return True
        else:
            return False
    else:
        if s%a==0:
            return True
        else:
            return False

=======
Suggestion 9

def solve(a,s):
    if a>s:
        return 'No'
    if a==s:
        return 'Yes'
    if a==0:
        return 'No'
    if a==1:
        return 'Yes'
    if s%2==0:
        return 'Yes'
    if a%2==0:
        return 'Yes'
    return 'No'

T = int(input())
for i in range(T):
    a,s = [int(x) for x in input().split()]
    print(solve(a,s))
