Synthesizing 9/10 solutions

=======
Suggestion 1

def get_weight(W):
    # 3个砝码的质量
    weight = [1, 2, 3]
    # 用于存储满足条件的砝码
    result = []
    # 用于存储��

=======
Suggestion 2

def main():
    w = int(input())
    if w <= 2:
        print(2)
        print(1, 2)
        return
    print(6)
    print(2, 5, 1, 2, 5, 1)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 4

def main():
    print("")

=======
Suggestion 5

def solve():
    W = int(input())
    if W <= 2:
        print(1)
        print(W)
        return
    if W <= 4:
        print(2)
        print(1, W - 1)
        return
    if W <= 6:
        print(3)
        print(1, 2, W - 3)
        return
    print(4)
    print(1, 2, 3, W - 6)
    return

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def solve():
    W = int(input())
    if W <= 3:
        print(1)
        print(W)
    elif W <= 5:
        print(2)
        print(1, W - 1)
    elif W <= 8:
        print(3)
        print(1, W - 2, 1)
    elif W <= 11:
        print(4)
        print(1, W - 3, 2, 1)
    else:
        print(6)
        print(1, W - 5, 2, 2, 2, 1)

=======
Suggestion 8

def solve(w):
    if w == 1:
        return [1]
    elif w == 2:
        return [1, 2]
    elif w == 3:
        return [1, 2, 3]
    elif w == 4:
        return [1, 2, 3, 4]
    elif w == 5:
        return [1, 2, 3, 4, 5]
    elif w == 6:
        return [1, 2, 3, 4, 5, 6]
    elif w == 7:
        return [1, 2, 3, 4, 5, 6, 7]
    elif w == 8:
        return [1, 2, 3, 4, 5, 6, 7, 8]
    elif w == 9:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9]
    elif w == 10:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    elif w == 11:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    elif w == 12:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
    elif w == 13:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]
    elif w == 14:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14]
    elif w == 15:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14, 15]
    elif w == 16:
        return [1, 2, 3, 4, 5

=======
Suggestion 9

def main():
    w = int(input())
    if w == 1:
        print(1)
        print(1)
        return
    if w == 2:
        print(2)
        print(1, 1)
        return
    if w == 3:
        print(2)
        print(1, 2)
        return
    if w == 4:
        print(2)
        print(1, 3)
        return
    if w == 5:
        print(3)
        print(1, 2, 2)
        return
    if w == 6:
        print(3)
        print(1, 2, 3)
        return
    if w == 7:
        print(3)
        print(1, 2, 4)
        return
    if w == 8:
        print(3)
        print(1, 2, 5)
        return
    if w == 9:
        print(3)
        print(1, 2, 6)
        return
    if w == 10:
        print(3)
        print(1, 2, 7)
        return
    if w == 11:
        print(3)
        print(1, 2, 8)
        return
    if w == 12:
        print(6)
        print(1, 2, 3, 2, 5, 1)
        return
    if w == 13:
        print(6)
        print(1, 2, 3, 2, 5, 1)
        return
    if w == 14:
        print(6)
        print(1, 2, 3, 2, 5, 1)
        return
    if w == 15:
        print(6)
        print(1, 2, 3, 2, 5, 1)
        return
    if w == 16:
        print(6)
        print(1, 2, 3, 2, 5, 1)
        return
    if w == 17:
        print(6)
        print(1, 2, 3, 2, 5, 1)
        return
    if w == 18:
        print(6
