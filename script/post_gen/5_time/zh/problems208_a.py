Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    A, B = map(int, input().split())
    if 6 * A < B:
        print("No")
    elif B <= A:
        print("Yes")
    else:
        print("Yes")

solve()

=======
Suggestion 2

def dice_sum(A, B):
    if A > 100 or A < 1:
        return False
    if B > 1000 or B < 1:
        return False

    if A == 1 and B < 7:
        return True
    elif A == 1 and B > 6:
        return False

    if B > 6 * A or B < A:
        return False

    if B == 6 * A:
        return True

    if B % A == 0:
        return True
    else:
        return False

=======
Suggestion 3

def main():
    a = input()
    b = input()
    if 100 >= int(a) >= 1 and 1000 >= int(b) >= 1:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 4

def main():
    #输入
    A, B = map(int, input().split())
    #处理
    if A <= B <= 6 * A:
        print("Yes")
    else:
        print("No")
    #输出

=======
Suggestion 5

def dice():
    a, b = map(int, input().split())
    for i in range(1, a+1):
        for j in range(1, a+1):
            if i + j == b:
                print("Yes")
                return
    print("No")

dice()

=======
Suggestion 6

def dice_sum(A,B):
    if A > 100 or A < 1 or B > 1000 or B < 1:
        return "No"
    elif A == 1 and B <= 6:
        return "Yes"
    elif A == 1 and B > 6:
        return "No"
    elif A == 2 and B <= 12:
        return "Yes"
    elif A == 2 and B > 12:
        return "No"
    elif A == 3 and B <= 18:
        return "Yes"
    elif A == 3 and B > 18:
        return "No"
    elif A == 4 and B <= 24:
        return "Yes"
    elif A == 4 and B > 24:
        return "No"
    elif A == 5 and B <= 30:
        return "Yes"
    elif A == 5 and B > 30:
        return "No"
    elif A == 6 and B <= 36:
        return "Yes"
    elif A == 6 and B > 36:
        return "No"
    elif A == 7 and B <= 42:
        return "Yes"
    elif A == 7 and B > 42:
        return "No"
    elif A == 8 and B <= 48:
        return "Yes"
    elif A == 8 and B > 48:
        return "No"
    elif A == 9 and B <= 54:
        return "Yes"
    elif A == 9 and B > 54:
        return "No"
    elif A == 10 and B <= 60:
        return "Yes"
    elif A == 10 and B > 60:
        return "No"
    elif A == 11 and B <= 66:
        return "Yes"
    elif A == 11 and B > 66:
        return "No"
    elif A == 12 and B <= 72:
        return "Yes"
    elif A == 12 and B > 72:
        return "No"
    elif A == 13 and B <= 78:
        return "Yes"
    elif A == 13 and B > 78:
        return "No"
    elif A == 14 and B <= 84:
        return "Yes"
    elif A == 14 and B

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    for i in range(1, a + 1):
        for j in range(1, 7):
            if i * j == b:
                print("Yes")
                return
    print("No")

=======
Suggestion 8

def main():
    A,B = map(int,input().split())
    if B % A == 0 and A <= B/6:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def solve():
    A, B = map(int, input().split())
    if B <= 6 * A and B >= A:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def solve():
    a, b = map(int, input().split())
    if a * 6 >= b and a <= b:
        print("Yes")
    else:
        print("No")
