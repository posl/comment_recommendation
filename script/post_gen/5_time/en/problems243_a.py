Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    v, a, b, c = map(int, input().split())
    while v > 0:
        v -= a
        if v <= 0:
            print('F')
            break
        v -= b
        if v <= 0:
            print('M')
            break
        v -= c
        if v <= 0:
            print('T')
            break

=======
Suggestion 2

def problems243_a():
    v,a,b,c = map(int, input().split())
    while v >= 0:
        v -= a
        if v < 0:
            print("F")
            break
        v -= b
        if v < 0:
            print("M")
            break
        v -= c
        if v < 0:
            print("T")
            break

=======
Suggestion 3

def main():
    v, a, b, c = map(int, input().split())
    shampoo = [a, b, c]
    while v > 0:
        for i in range(3):
            v -= shampoo[i]
            if v < 0:
                if i == 0:
                    print("F")
                elif i == 1:
                    print("M")
                else:
                    print("T")
                return 0

=======
Suggestion 4

def solve():
    v,a,b,c = map(int,input().split())
    while v >= 0:
        v -= a
        if v < 0:
            print('F')
            return
        v -= b
        if v < 0:
            print('M')
            return
        v -= c
        if v < 0:
            print('T')
            return

=======
Suggestion 5

def main():
    v,a,b,c = map(int, input().split())
    if a >= v:
        print("F")
    elif a+b >= v:
        print("M")
    else:
        print("T")

=======
Suggestion 6

def problems243_a():
    v, a, b, c = map(int, input().split())
    if v >= c:
        v -= c
        if v >= b:
            v -= b
            if v >= a:
                print('T')
            else:
                print('F')
        else:
            print('M')
    else:
        print('F')

=======
Suggestion 7

def shampoo():
    v,a,b,c = map(int,input().split())
    while v > 0:
        v -= a
        if v <= 0:
            print('F')
            return
        v -= b
        if v <= 0:
            print('M')
            return
        v -= c
        if v <= 0:
            print('T')
            return

=======
Suggestion 8

def func(v,a,b,c):
    if v <= a:
        return 'F'
    elif v <= a+b:
        return 'M'
    elif v <= a+b+c:
        return 'T'
    else:
        return None

=======
Suggestion 9

def solve():
    v, a, b, c = map(int, input().split())
    if a >= v:
        print("F")
    elif a < v and b >= (v - a):
        print("M")
    elif a < v and b < (v - a) and c >= (v - a - b):
        print("T")
    else:
        print("T")

=======
Suggestion 10

def problems243_a():
    v,a,b,c = map(int,input().split())
    shampoo = [a,b,c]
    shampoo.sort()
    shampoo.reverse()
    while v>0:
        for i in range(3):
            v -= shampoo[i]
            if v<=0:
                if i == 0:
                    print('F')
                elif i == 1:
                    print('M')
                else:
                    print('T')
                return
    return
