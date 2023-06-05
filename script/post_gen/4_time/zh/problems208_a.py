Synthesizing 10/10 solutions

=======
Suggestion 1

def f(n, m):
    if n > m:
        return "No"
    elif n == m:
        return "Yes"
    else:
        return f(n+6, m)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    for i in range(1, A+1):
        for j in range(1, A+1):
            if i + j == B:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 3

def throw_dice(n, m):
    if (n < 1 or m < 1):
        return False
    if (n == 1):
        if (m >= 1 and m <= 6):
            return True
        else:
            return False
    else:
        return throw_dice(n - 1, m - 1) or throw_dice(n - 1, m - 2) or throw_dice(n - 1, m - 3) or throw_dice(n - 1, m - 4) or throw_dice(n - 1, m - 5) or throw_dice(n - 1, m - 6)

print(throw_dice(100, 600))
print(throw_dice(2, 13))
print(throw_dice(2, 11))

=======
Suggestion 4

def check(A,B):
    if A*6 >= B and A <= B:
        return True
    else:
        return False

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    if a <= b <= 6*a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if a*1 <= b <= a*6:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def solve(A,B):
    for i in range(1,7):
        for j in range(1,7):
            if i+j==B:
                return True
    return False

A,B=map(int,input().split())

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    if a <= b <= a*6:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def dice_sum(n, s):
    if n == 1 and s <= 6:
        return True
    elif n == 1:
        return False
    else:
        for i in range(1, 7):
            if dice_sum(n-1, s-i):
                return True
        return False

=======
Suggestion 10

def main():
    A,B = map(int,raw_input().split())
    for i in range(1,7):
        for j in range(1,7):
            if A*i + j == B:
                print "Yes"
                return
    print "No"
