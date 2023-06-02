Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    v,a,b,c = map(int, input().split())
    if v % 3 == 0:
        print("F")
    elif v % 3 == 1:
        print("M")
    elif v % 3 == 2:
        print("T")

=======
Suggestion 2

def main():
    v,a,b,c = map(int,input().split())
    if v%a == 0:
        print('F')
    elif v%b == 0:
        print('M')
    elif v%c == 0:
        print('T')

=======
Suggestion 3

def solve():
    v,a,b,c=map(int,input().split())
    while True:
        if v<=0:
            print('F')
            break
        v-=a
        if v<=0:
            print('F')
            break
        v-=b
        if v<=0:
            print('M')
            break
        v-=c
        if v<=0:
            print('T')
            break

=======
Suggestion 4

def main():
    v,a,b,c = map(int,input().split())
    while(True):
        if(v >= a):
            v -= a
        else:
            print("F")
            break
        if(v >= b):
            v -= b
        else:
            print("M")
            break
        if(v >= c):
            v -= c
        else:
            print("T")
            break

=======
Suggestion 5

def problems243_a():
    pass

=======
Suggestion 6

def main():
    v,a,b,c = map(int,input().split())
    while v > 0:
        if a > 0:
            v -= a
            if v < 0:
                print('F')
                break
        if b > 0:
            v -= b
            if v < 0:
                print('M')
                break
        if c > 0:
            v -= c
            if v < 0:
                print('T')
                break

=======
Suggestion 7

def main():
    v,a,b,c = map(int,input().split())
    while v > 0:
        a -= 1
        v -= 1
        if a == 0:
            print("F")
            return
        b -= 1
        v -= 1
        if b == 0:
            print("M")
            return
        c -= 1
        v -= 1
        if c == 0:
            print("T")
            return

=======
Suggestion 8

def problem243_a():
    v,a,b,c=map(int,input().split())
    while v>=0:
        v-=a
        if v<0:
            print('F')
            break
        v-=b
        if v<0:
            print('M')
            break
        v-=c
        if v<0:
            print('T')
            break

=======
Suggestion 9

def problem243_a():
    v,a,b,c = map(int,input().split())
    if v < a:
        print("F")
    elif v < b:
        print("M")
    elif v < c:
        print("T")
    else:
        print("T")

=======
Suggestion 10

def main():
    v,a,b,c = map(int, input().split())
    while True:
        if v >= a:
            v -= a
        else:
            print('F')
            break
        if v >= b:
            v -= b
        else:
            print('M')
            break
        if v >= c:
            v -= c
        else:
            print('T')
            break
