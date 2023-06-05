Synthesizing 10/10 solutions

=======
Suggestion 1

def problems243_a():
    v,a,b,c = map(int, input().split())
    while v > 0:
        if v < a:
            print("F")
            break
        v -= a
        if v < b:
            print("M")
            break
        v -= b
        if v < c:
            print("T")
            break
        v -= c

=======
Suggestion 2

def main():
    v,a,b,c = map(int, input().split())
    while v > 0:
        if v >= a:
            v -= a
        else:
            print("F")
            return
        if v >= b:
            v -= b
        else:
            print("M")
            return
        if v >= c:
            v -= c
        else:
            print("T")
            return

=======
Suggestion 3

def main():
    v,a,b,c = map(int,input().split())
    while v >= 0:
        v -= a
        if v < 0:
            print('T')
            break
        v -= b
        if v < 0:
            print('M')
            break
        v -= c
        if v < 0:
            print('F')
            break

=======
Suggestion 4

def problems243_a():
    v,a,b,c = map(int, input().split())
    while True:
        if v == 0:
            print('F')
            break
        v -= a
        if v == 0:
            print('F')
            break
        v -= b
        if v == 0:
            print('M')
            break
        v -= c
        if v == 0:
            print('T')
            break

=======
Suggestion 5

def solve():
    v,a,b,c = map(int, input().split())
    while True:
        if v < a:
            return 'F'
        v -= a
        if v < b:
            return 'M'
        v -= b
        if v < c:
            return 'T'
        v -= c

print(solve())

=======
Suggestion 6

def main():
    v,a,b,c = map(int,input().split())
    while True:
        if v < a:
            print("F")
            break
        else:
            v -= a
        if v < b:
            print("M")
            break
        else:
            v -= b
        if v < c:
            print("T")
            break
        else:
            v -= c

=======
Suggestion 7

def problems243_a():
    v,a,b,c = map(int, input().split())
    while v > 0:
        if v - a < 0:
            return 'F'
        v -= a
        if v - b < 0:
            return 'M'
        v -= b
        if v - c < 0:
            return 'T'
        v -= c

print(problems243_a())

=======
Suggestion 8

def main():
    v,a,b,c = map(int,input().split())
    if (v%a==0) or (v%b==0) or (v%c==0):
        print("T")
    else:
        print("F")

=======
Suggestion 9

def main():
    v,a,b,c = map(int, input().split())
    while True:
        v -= a
        if v < 0:
            print('F')
            break
        v -= b
        if v < 0:
            print('M')
            break
        v -= c
        if v < 0:
            print('T')
            break

=======
Suggestion 10

def problems243_a():
    v, a, b, c = map(int, input().split())
    while v > 0:
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
