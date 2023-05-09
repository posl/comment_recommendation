Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a * 1 <= b <= a * 6:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a * 1 <= b <= a * 6:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def solve():
    a, b = map(int, input().split())
    if a * 1 <= b <= a * 6:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a <= b <= 6 * a:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if A*1 <= B and A*6 >= B:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    A, B = map(int, input().split())

    if (A <= B and B <= 6*A):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def check_sum(a,b):
    for i in range(1,7):
        for j in range(1,7):
            if i+j == b:
                return 'Yes'
    return 'No'

a,b = map(int,input().split())
print(check_sum(a,b))

=======
Suggestion 8

def solve():
    A, B = list(map(int, input().split()))
    if A <= B <= 6*A:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def dice_probability(a, b):
    if a <= 0:
        return False
    elif a == 1:
        if b <= 6:
            return True
        else:
            return False
    elif a == 2:
        if b == 2 or b == 3 or b == 4 or b == 5 or b == 6 or b == 7 or b == 8 or b == 9 or b == 10 or b == 11 or b == 12:
            return True
        else:
            return False
    elif a == 3:
        if b == 3 or b == 4 or b == 5 or b == 6 or b == 7 or b == 8 or b == 9 or b == 10 or b == 11 or b == 12 or b == 13 or b == 14 or b == 15 or b == 16 or b == 17 or b == 18:
            return True
        else:
            return False
    elif a == 4:
        if b == 4 or b == 5 or b == 6 or b == 7 or b == 8 or b == 9 or b == 10 or b == 11 or b == 12 or b == 13 or b == 14 or b == 15 or b == 16 or b == 17 or b == 18 or b == 19 or b == 20 or b == 21 or b == 22 or b == 23 or b == 24:
            return True
        else:
            return False
    elif a == 5:
        if b == 5 or b == 6 or b == 7 or b == 8 or b == 9 or b == 10 or b == 11 or b == 12 or b == 13 or b == 14 or b == 15 or b == 16 or b == 17 or b == 18 or b == 19 or b == 20 or b == 21 or b == 22 or b == 23 or b == 24 or b == 25 or b == 26 or b == 27 or b == 28 or b == 29 or b == 30 or b == 31 or b == 32 or b == 33 or b == 34
