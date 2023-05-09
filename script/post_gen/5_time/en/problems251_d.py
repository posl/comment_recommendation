Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    W = int(input())
    if W == 1:
        print(1)
        print(1)
    elif W == 2:
        print(2)
        print(1,1)
    elif W == 3:
        print(2)
        print(1,2)
    elif W == 4:
        print(3)
        print(1,2,1)
    elif W == 5:
        print(3)
        print(1,2,2)
    elif W == 6:
        print(3)
        print(1,2,3)
    elif W == 7:
        print(3)
        print(1,2,4)
    elif W == 8:
        print(4)
        print(1,2,2,3)
    elif W == 9:
        print(4)
        print(1,2,2,4)
    elif W == 10:
        print(4)
        print(1,2,3,4)
    elif W == 11:
        print(4)
        print(1,2,3,5)
    elif W == 12:
        print(4)
        print(1,2,3,6)
    else:
        print(5)
        print(1,2,3,4,5)

=======
Suggestion 2

def main():
    w = int(input())
    if w == 1:
        print(1)
        print(1)
        return
    if w == 2:
        print(2)
        print(1, 2)
        return
    if w == 3:
        print(2)
        print(1, 2)
        return
    if w == 4:
        print(3)
        print(1, 2, 4)
        return
    if w == 5:
        print(3)
        print(1, 2, 4)
        return
    if w == 6:
        print(3)
        print(1, 2, 3)
        return
    if w == 7:
        print(3)
        print(1, 2, 3)
        return
    if w == 8:
        print(4)
        print(1, 2, 4, 8)
        return
    if w == 9:
        print(4)
        print(1, 2, 4, 8)
        return
    if w == 10:
        print(4)
        print(1, 2, 3, 10)
        return
    if w == 11:
        print(4)
        print(1, 2, 3, 10)
        return
    if w == 12:
        print(4)
        print(1, 2, 3, 12)
        return
    if w == 13:
        print(4)
        print(1, 2, 3, 12)
        return
    if w == 14:
        print(4)
        print(1, 2, 3, 12)
        return
    if w == 15:
        print(4)
        print(1, 2, 3, 12)
        return
    if w == 16:
        print(5)
        print(1, 2, 4, 8, 16)
        return
    if w == 17:
        print(5)
        print(1, 2, 4, 8, 16)
        return
    if w == 18:
        print(5)
        print(1, 2, 3, 6,

=======
Suggestion 3

def main():
    W = int(input())
    if W <= 3:
        print(1)
        print(W)
    elif W <= 5:
        print(2)
        print(2, W-2)
    else:
        print(3)
        print(2, 3, W-5)

=======
Suggestion 4

def main():
    w = int(input())
    if w <= 2:
        print(2)
        print(1, 1)
    elif w <= 3:
        print(2)
        print(1, 2)
    elif w <= 4:
        print(3)
        print(1, 2, 1)
    elif w <= 5:
        print(3)
        print(1, 2, 2)
    elif w <= 6:
        print(3)
        print(1, 2, 3)
    elif w <= 7:
        print(3)
        print(1, 2, 4)
    elif w <= 8:
        print(3)
        print(1, 2, 5)
    elif w <= 9:
        print(3)
        print(1, 2, 6)
    elif w <= 10:
        print(3)
        print(1, 2, 7)
    elif w <= 11:
        print(3)
        print(1, 2, 8)
    elif w <= 12:
        print(3)
        print(1, 2, 9)
    elif w <= 13:
        print(3)
        print(1, 2, 10)
    elif w <= 14:
        print(3)
        print(1, 2, 11)
    elif w <= 15:
        print(3)
        print(1, 2, 12)
    elif w <= 16:
        print(3)
        print(1, 2, 13)
    elif w <= 17:
        print(3)
        print(1, 2, 14)
    elif w <= 18:
        print(3)
        print(1, 2, 15)
    elif w <= 19:
        print(3)
        print(1, 2, 16)
    elif w <= 20:
        print(3)
        print(1, 2, 17)
    elif w <= 21:
        print(3)
        print(1, 2, 18)
    elif w <= 22:
        print(3)
        print(1, 2, 19)
    elif w <= 23:
        print(3)
        print(

=======
Suggestion 5

def solve():
    w = int(input())
    if w == 3:
        print(2)
        print(1,2)
    elif w == 2:
        print(2)
        print(1,1)
    elif w == 1:
        print(1)
        print(1)
    elif w == 4:
        print(2)
        print(1,3)
    elif w == 5:
        print(2)
        print(2,3)
    elif w == 6:
        print(3)
        print(1,2,3)
    elif w == 7:
        print(3)
        print(1,2,4)
    elif w == 8:
        print(3)
        print(1,2,5)
    elif w == 9:
        print(3)
        print(1,2,6)
    elif w == 10:
        print(3)
        print(1,2,7)
    elif w == 11:
        print(3)
        print(1,2,8)
    elif w == 12:
        print(4)
        print(1,2,3,6)
    elif w == 13:
        print(4)
        print(1,2,3,7)
    elif w == 14:
        print(4)
        print(1,2,3,8)
    elif w == 15:
        print(4)
        print(1,2,3,9)
    elif w == 16:
        print(4)
        print(1,2,3,10)
    elif w == 17:
        print(4)
        print(1,2,3,11)
    elif w == 18:
        print(4)
        print(1,2,3,12)
    elif w == 19:
        print(4)
        print(1,2,4,12)
    elif w == 20:
        print(4)
        print(1,2,5,12)
    elif w == 21:
        print(4)
        print(1,2,6,12)
    elif w == 22:
        print(4)
        print(1,2,7,12)
    elif w == 23:
        print(4)
        print(1,2,8

=======
Suggestion 6

def main():
    W = int(input())
    if W <= 2:
        print(2)
        print(1, 1)
        return
    if W <= 3:
        print(2)
        print(1, 2)
        return
    print(3)
    print(1, 2, 3)
    return

=======
Suggestion 7

def solve():
    w = int(input())
    if w <= 2:
        print(2)
        print(1, 1)
    else:
        print(w)
        if w % 2 == 0:
            for i in range(w//2):
                print(2, end=' ')
        else:
            for i in range(w//2-1):
                print(2, end=' ')
            print(3)
solve()

=======
Suggestion 8

def main():
    W = int(input())
    if W <= 2:
        print(2)
        print(1, 1)
    else:
        print(W//2 + W%2)
        print(1 + (W%2), *(2 for _ in range(W//2)))

=======
Suggestion 9

def solve():
    W = int(input())
    N = 300
    A = [1, 2, 3]
    for i in range(4, W+1):
        if i%6 == 0:
            A.append(i)
    print(N)
    print(" ".join(map(str, A)))

=======
Suggestion 10

def solve(W):
    if W <= 300:
        return W
    else:
        return "NG"
