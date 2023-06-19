Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    v,a,b,c = map(int,input().split())
    while v > 0:
        v -= a
        if v <= 0:
            print("T")
            break
        v -= b
        if v <= 0:
            print("M")
            break
        v -= c
        if v <= 0:
            print("F")
            break

=======
Suggestion 2

def main():
    v,a,b,c = map(int,input().split())
    while v:
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
Suggestion 3

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

=======
Suggestion 4

def problems243_a():
    v,a,b,c = map(int,input().split())
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
Suggestion 5

def problems243_a():
    v,a,b,c = map(int, input().split())
    while v > 0:
        v = v - a
        if v < 0:
            print('F')
            return
        v = v - b
        if v < 0:
            print('M')
            return
        v = v - c
        if v < 0:
            print('T')
            return
    return

problems243_a()

=======
Suggestion 6

def problems243_a():
    v,a,b,c = map(int, input().strip().split())
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
Suggestion 7

def washHair(v, a, b, c):
    if v < a:
        return 'F'
    elif v < a + b:
        return 'M'
    else:
        return 'T'

=======
Suggestion 8

def main():
    v,a,b,c=map(int,input().split())
    while v>0:
        v-=a
        if v<0:
            print("F")
            break
        v-=b
        if v<0:
            print("M")
            break
        v-=c
        if v<0:
            print("T")
            break

=======
Suggestion 9

def main():
    # 读取输入
    v, a, b, c = map(int, input().split())
    # 处理
    if v < a:
        print("F")
        return
    v -= a
    if v < b:
        print("M")
        return
    v -= b
    if v < c:
        print("T")
        return
    print("T")

=======
Suggestion 10

def problems243_a():
    v,a,b,c = map(int, input().split())
    if v <= a:
        print('F')
    elif v <= a + b:
        print('M')
    else:
        print('T')
