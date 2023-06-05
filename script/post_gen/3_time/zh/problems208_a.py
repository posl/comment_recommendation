Synthesizing 10/10 solutions

=======
Suggestion 1

def DiceSum(A,B):
    if A*1<=B<=A*6:
        return "Yes"
    else:
        return "No"

=======
Suggestion 2

def solve():
    A, B = map(int, input().split())
    for i in range(1, A+1):
        for j in range(1, A+1):
            if (i + j) == B:
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def throw_dice(num, target):
    if num == 1:
        if 1 <= target <= 6:
            return True
        else:
            return False
    else:
        for i in range(1, 7):
            if throw_dice(num-1, target - i):
                return True
        return False

=======
Suggestion 4

def dice_sum(a,b):
    for i in range(1,7):
        for j in range(1,7):
            if a*i+j == b:
                return True
    return False

=======
Suggestion 5

def main():
    A,B = map(int,input().split())
    if A <= 100 and A >= 1 and B <= 1000 and B >= 1:
        if B % 2 == 0:
            if A <= B / 2:
                print("Yes")
            else:
                print("No")
        else:
            if A <= B / 2 + 1:
                print("Yes")
            else:
                print("No")
    else:
        print("No")

=======
Suggestion 6

def solve():
    a, b = map(int, input().split())
    print("Yes" if 6 * a >= b and b >= a else "No")
    return 0

=======
Suggestion 7

def is_sum_possible(a, b):
	if a > b:
		return False
	if a * 6 < b:
		return False
	return True

=======
Suggestion 8

def main():
    # 读取输入
    A,B = map(int,input().split())
    # print("A = ",A," B = ",B)

    # 判断是否能得到B
    if A <= B <= A * 6:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def get_sum(A,B):
    if A == 1:
        if B < 7:
            return "Yes"
        else:
            return "No"
    elif A == 2:
        if B < 13:
            return "Yes"
        else:
            return "No"
    elif A == 3:
        if B < 19:
            return "Yes"
        else:
            return "No"
    elif A == 4:
        if B < 25:
            return "Yes"
        else:
            return "No"
    elif A == 5:
        if B < 31:
            return "Yes"
        else:
            return "No"
    elif A == 6:
        if B < 37:
            return "Yes"
        else:
            return "No"
    elif A == 7:
        if B < 43:
            return "Yes"
        else:
            return "No"
    elif A == 8:
        if B < 49:
            return "Yes"
        else:
            return "No"
    elif A == 9:
        if B < 55:
            return "Yes"
        else:
            return "No"
    elif A == 10:
        if B < 61:
            return "Yes"
        else:
            return "No"
    elif A == 11:
        if B < 67:
            return "Yes"
        else:
            return "No"
    elif A == 12:
        if B < 73:
            return "Yes"
        else:
            return "No"
    elif A == 13:
        if B < 79:
            return "Yes"
        else:
            return "No"
    elif A == 14:
        if B < 85:
            return "Yes"
        else:
            return "No"
    elif A == 15:
        if B < 91:
            return "Yes"
        else:
            return "No"
    elif A == 16:
        if B < 97:
            return "Yes"
        else:
            return "No"
    elif A == 17:
        if B < 103:
            return "Yes"
        else:
            return "No"
    elif A == 18:
        if B < 109:
            return "Yes"
        else:
            return "No"
    elif A == 19:
        if

=======
Suggestion 10

def main():
    a, b = map(int, input().split())
    if a*6 >= b and a <= b:
        print("Yes")
    else:
        print("No")
