Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == b and a == 2:
                print('Yes')
                return
    print('No')

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A * 6 < B:
        print('No')
    elif A > B:
        print('No')
    else:
        print('Yes')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a * 6 < b:
        print('No')
    elif a > b:
        print('No')
    else:
        print('Yes')

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    for i in range(a + 1):
        for j in range(a + 1):
            if i + j == b:
                print("Yes")
                return
    print("No")

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    for i in range(a):
        for j in range(a):
            if (i + 1) + (j + 1) == b:
                print("Yes")
                return
    print("No")

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    for i in range(A+1):
        for j in range(A+1):
            if 6*i+1*j == B:
                print('Yes')
                return
    print('No')

=======
Suggestion 7

def main():
    a,b = map(int, input().split())
    if 6*a < b:
        print("No")
    elif b < a:
        print("No")
    else:
        print("Yes")

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if a >= b:
        print('Yes')
    elif a == 1:
        print('No')
    elif a == 2:
        if b % 2 == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')

=======
Suggestion 9

def dice_sum(A, B):
    if A * 1 > B or A * 6 < B:
        return 'No'
    else:
        return 'Yes'

A, B = map(int, input().split())

print(dice_sum(A, B))

=======
Suggestion 10

def solve(A,B):
    if A*1 <= B <= A*6:
        return "Yes"
    else:
        return "No"
