Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    T = int(input())
    for i in range(T):
        a, s = map(int, input().split())
        if a > s:
            print("No")
        else:
            print("Yes")

=======
Suggestion 2

def solve(a, s):
    if a > s:
        return 'No'
    elif (s - a) % 2 == 0:
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 3

def solve(a,s):
    if a > s:
        return "No"
    if (s-a)%2 == 0:
        return "Yes"
    else:
        return "No"

=======
Suggestion 4

def main():
    t = int(input())
    for i in range(t):
        a,s = map(int, input().split())
        if a>s:
            print("No")
        else:
            if a == s:
                print("Yes")
            else:
                if (s-a)%2 == 0:
                    print("Yes")
                else:
                    print("No")
main()

=======
Suggestion 5

def main():
    N = int(input())
    for i in range(N):
        a, s = map(int, input().split())
        if s < a:
            print('No')
        else:
            if (s - a) % 2 == 0:
                print('Yes')
            else:
                print('No')

=======
Suggestion 6

def check(a, s):
    if a > s:
        return False
    if a == 0:
        return s == 0
    if a == s:
        return True
    if a == 1:
        return False
    if a == 2:
        return s == 2
    if a == 3:
        return s == 2 or s == 3
    if a == 4:
        return s == 4
    if a == 5:
        return s == 4 or s == 5
    if a == 6:
        return s == 4 or s == 5 or s == 6
    if a == 7:
        return s == 4 or s == 5 or s == 6 or s == 7
    if a == 8:
        return s == 8
    if a == 9:
        return s == 8 or s == 9
    if a == 10:
        return s == 8 or s == 9 or s == 10
    if a == 11:
        return s == 8 or s == 9 or s == 10 or s == 11
    if a == 12:
        return s == 12
    if a == 13:
        return s == 12 or s == 13
    if a == 14:
        return s == 12 or s == 13 or s == 14
    if a == 15:
        return s == 12 or s == 13 or s == 14 or s == 15
    if a == 16:
        return s == 16
    if a == 17:
        return s == 16 or s == 17
    if a == 18:
        return s == 16 or s == 17 or s == 18
    if a == 19:
        return s == 16 or s == 17 or s == 18 or s == 19
    if a == 20:
        return s == 20
    if a == 21:
        return s == 20 or s == 21
    if a == 22:
        return s == 20 or s == 21 or s == 22
    if a == 23:
        return s == 20 or s ==

=======
Suggestion 7

def solve(a, s):
    if a == s:
        return "Yes"
    if a > s:
        return "No"
    if a == 0:
        return "No"
    if (s - a) % 2 == 0:
        return "Yes"
    return "No"

=======
Suggestion 8

def solve(a,s):
    if (a > s):
        return "No"
    if (a == 0):
        return "Yes"
    if (a == s):
        return "Yes"
    if (a == 1):
        if (s == 1):
            return "Yes"
        else:
            return "No"
    if (a == 2):
        if (s == 3):
            return "Yes"
        else:
            return "No"
    if (a == 3):
        if (s == 2):
            return "Yes"
        else:
            return "No"
    if (a == 4):
        if (s == 6):
            return "Yes"
        else:
            return "No"
    if (a == 5):
        if (s == 7):
            return "Yes"
        else:
            return "No"
    if (a == 6):
        if (s == 4):
            return "Yes"
        else:
            return "No"
    if (a == 7):
        if (s == 5):
            return "Yes"
        else:
            return "No"
    if (a == 8):
        if (s == 15):
            return "Yes"
        else:
            return "No"
    if (a == 9):
        if (s == 14):
            return "Yes"
        else:
            return "No"
    if (a == 10):
        if (s == 12):
            return "Yes"
        else:
            return "No"
    if (a == 11):
        if (s == 13):
            return "Yes"
        else:
            return "No"
    if (a == 12):
        if (s == 10):
            return "Yes"
        else:
            return "No"
    if (a == 13):
        if (s == 11):
            return "Yes"
        else:
            return "No"
    if (a == 14):
        if (s == 9):
            return "Yes"
        else:
            return "No"
    if (a == 15):
        if (s == 8):
            return "Yes"
        else:
            return "No"
    if (a == 16):
        if (s == 31):
            return "Yes"
        else:

=======
Suggestion 9

def solve():
    a, s = map(int, input().split())
    if a > s:
        print('No')
        return
    if s % 2 == 0:
        print('Yes')
        return
    if s % 2 == 1 and a % 2 == 1:
        print('Yes')
        return
    print('No')

T = int(input())
for _ in range(T):
    solve()

=======
Suggestion 10

def isPowerOfTwo(n):
    if n==0:
        return False
    return n & (n-1) == 0
