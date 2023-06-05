Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    w = int(input())
    print(3)
    print(1, 2, w-3)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    w = int(input())
    if w < 3:
        print(1)
        print(w)
    else:
        print(2)
        print(w // 2, w - w // 2)

=======
Suggestion 4

def solve():
    w = int(input())
    if w <= 2:
        print(2)
        print(1, 1)
    elif w <= 5:
        print(2)
        print(2, 3)
    else:
        print(6)
        print(1, 2, 4, 5, 7, 8)
solve()

=======
Suggestion 5

def main():
    w = int(input())
    if w == 3:
        print(2)
        print(1, 2)
    elif w == 2:
        print(2)
        print(1, 2)
    elif w == 1:
        print(1)
        print(1)
    elif w == 4:
        print(3)
        print(1, 2, 3)
    elif w == 5:
        print(3)
        print(1, 2, 3)
    elif w == 6:
        print(3)
        print(1, 2, 3)
    elif w == 7:
        print(3)
        print(1, 2, 4)
    elif w == 8:
        print(3)
        print(1, 2, 5)
    elif w == 9:
        print(3)
        print(1, 2, 6)
    elif w == 10:
        print(3)
        print(1, 2, 7)
    elif w == 11:
        print(3)
        print(1, 2, 8)
    elif w == 12:
        print(3)
        print(1, 2, 9)
    elif w == 13:
        print(3)
        print(1, 2, 10)
    elif w == 14:
        print(3)
        print(1, 2, 11)
    elif w == 15:
        print(3)
        print(1, 2, 12)
    elif w == 16:
        print(3)
        print(1, 2, 13)
    elif w == 17:
        print(3)
        print(1, 2, 14)
    elif w == 18:
        print(3)
        print(1, 2, 15)
    elif w == 19:
        print(3)
        print(1, 2, 16)
    elif w == 20:
        print(3)
        print(1, 2, 17)
    elif w == 21:
        print(3)
        print(1, 2, 18)
    elif w == 22:
        print(3)
        print(1, 2,

=======
Suggestion 6

def main():
    w = int(input())
    print(6)
    print("2 5 1 2 5 1")
    return

=======
Suggestion 7

def get_good_integers(w):
    if w == 1:
        return [1]
    if w == 2:
        return [1,2]
    if w == 3:
        return [1,2,3]
    if w == 4:
        return [1,2,3,4]
    if w == 5:
        return [1,2,3,4,5]
    if w == 6:
        return [1,2,3,4,5,6]
    if w == 7:
        return [1,2,3,4,5,6,7]
    if w == 8:
        return [1,2,3,4,5,6,7,8]
    if w == 9:
        return [1,2,3,4,5,6,7,8,9]
    if w == 10:
        return [1,2,3,4,5,6,7,8,9,10]
    if w == 11:
        return [1,2,3,4,5,6,7,8,9,10,11]
    if w == 12:
        return [1,2,3,4,5,6,7,8,9,10,11,12]
    if w == 13:
        return [1,2,3,4,5,6,7,8,9,10,11,12,13]
    if w == 14:
        return [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    if w == 15:
        return [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    if w == 16:
        return [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    if w == 17:
        return [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    if w == 18:
        return [1,2,3,4,

=======
Suggestion 8

def f(w):
    if w<=3:
        return [1,2,3][:w]
    elif w%2:
        return [1,2]+f(w-3)
    else:
        return [2,3]+f(w-5)

w=int(input())
l=f(w)
print(len(l))
print(*l)

=======
Suggestion 9

def solve(w):
    if w <= 3:
        return [w]

    if w % 2 == 0:
        return [2] + solve(w - 2)
    else:
        return [3] + solve(w - 3)

=======
Suggestion 10

def solve(n):
    if n <= 3:
        print(1)
        print(n)
        return
    elif n == 4:
        print(2)
        print(1, 2)
        return
    elif n == 5:
        print(2)
        print(2, 3)
        return
    elif n == 6:
        print(3)
        print(1, 2, 3)
        return
    else:
        print(3)
        print(1, 2, 4)
        return
