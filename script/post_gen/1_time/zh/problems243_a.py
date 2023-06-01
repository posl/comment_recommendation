Synthesizing 10/10 solutions

=======
Suggestion 1

def judge(v,a,b,c):
    if v>a:
        if v>b:
            if v>c:
                return True
    return False

=======
Suggestion 2

def main():
    v, a, b, c = map(int, input().split())
    v1 = v - a
    v2 = v - a - b
    v3 = v - a - b - c
    if v1 <= 0:
        print('F')
    elif v2 <= 0:
        print('M')
    else:
        print('T')

=======
Suggestion 3

def main():
    v,a,b,c = map(int, input().split())
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
Suggestion 4

def main():
    v,a,b,c = map(int, input().split())
    while v >= 0:
        if v >= c:
            v -= c
        else:
            print('T')
            break
        if v >= b:
            v -= b
        else:
            print('F')
            break
        if v >= a:
            v -= a
        else:
            print('M')
            break

=======
Suggestion 5

def problems243_a():
    v,a,b,c = map(int, input().split())
    if v % a == 0 or v % b == 0 or v % c == 0:
        print("T")
    else:
        print("F")

=======
Suggestion 6

def problems243_a():
    v,a,b,c = map(int, input().split())
    while v > 0:
        if v >= a:
            v -= a
        else:
            print('F')
            return
        if v >= b:
            v -= b
        else:
            print('M')
            return
        if v >= c:
            v -= c
        else:
            print('T')
            return
    print('T')

=======
Suggestion 7

def solve():
    v,a,b,c = map(int,input().split())
    while v >= 0:
        if v >= a:
            v -= a
        else:
            print("F")
            break
        if v >= b:
            v -= b
        else:
            print("M")
            break
        if v >= c:
            v -= c
        else:
            print("T")
            break
    return 0

=======
Suggestion 8

def problems243_a():
    v, a, b, c = map(int, input().split())
    while True:
        if v >= a:
            v -= a
        else:
            print("F")
            break
        if v >= b:
            v -= b
        else:
            print("M")
            break
        if v >= c:
            v -= c
        else:
            print("T")
            break

=======
Suggestion 9

def main():
    v,a,b,c = map(int, input().split())
    while True:
        if v < a:
            print('F')
            break
        else:
            v -= a
        if v < b:
            print('M')
            break
        else:
            v -= b
        if v < c:
            print('T')
            break
        else:
            v -= c

=======
Suggestion 10

def main():
    v,a,b,c = map(int, input().split())
    if (v % a == 0) or (v % b == 0) or (v % c == 0):
        print("T")
    else:
        print("F")
