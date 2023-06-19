Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    for i in range(1, a+1):
        for j in range(1, a+1):
            if i+j == b:
                print('Yes')
                exit()
    print('No')

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a * 6 >= b and a <= b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    for i in range(1, a+1):
        if b <= i*6 and b >= i*1:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    if a*6>=b and a<=b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def solve(a,b):
    if a*6 < b:
        return 'No'
    elif a <= b:
        return 'Yes'
    else:
        return 'No'

a,b = map(int,input().split())
print(solve(a,b))

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    if A*6 >= B and A <= B:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def dice_sum(A, B):
    for i in range(1, 7):
        for j in range(1, 7):
            if A == 2:
                if i + j == B:
                    return True
            elif A == 3:
                for k in range(1, 7):
                    if i + j + k == B:
                        return True
            elif A == 4:
                for k in range(1, 7):
                    for l in range(1, 7):
                        if i + j + k + l == B:
                            return True
            elif A == 5:
                for k in range(1, 7):
                    for l in range(1, 7):
                        for m in range(1, 7):
                            if i + j + k + l + m == B:
                                return True
            elif A == 6:
                for k in range(1, 7):
                    for l in range(1, 7):
                        for m in range(1, 7):
                            for n in range(1, 7):
                                if i + j + k + l + m + n == B:
                                    return True
            elif A == 7:
                for k in range(1, 7):
                    for l in range(1, 7):
                        for m in range(1, 7):
                            for n in range(1, 7):
                                for o in range(1, 7):
                                    if i + j + k + l + m + n + o == B:
                                        return True
            elif A == 8:
                for k in range(1, 7):
                    for l in range(1, 7):
                        for m in range(1, 7):
                            for n in range(1, 7):
                                for o in range(1, 7):
                                    for p in range(1, 7):
                                        if i + j + k + l + m + n + o + p == B:
                                            return True
            elif A == 9:
                for k in range(1, 7):
                    for l in range(1, 7):
                        for m in range(1, 7):
                            for n in range(1, 7):
                                for o in range(1, 7):
                                    for p in

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    if a * 6 < b or a > b:
        print('No')
    else:
        print('Yes')

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    if a <= b <= 6 * a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def dice_sum(A, B):
    if A <= 0:
        return False
    if A == 1:
        if B >= 1 and B <= 6:
            return True
        else:
            return False
    else:
        if B >= A and B <= 6 * A:
            return True
        else:
            return False
