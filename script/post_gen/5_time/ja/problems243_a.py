Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    v, a, b, c = map(int, input().split())
    while v > 0:
        if v - a <= 0:
            print("T")
            break
        if v - b <= 0:
            print("F")
            break
        if v - c <= 0:
            print("M")
            break

=======
Suggestion 2

def solve():
    v, a, b, c = map(int, input().split())
    while True:
        if v - a < 0:
            return "F"
        else:
            v -= a
        if v - b < 0:
            return "M"
        else:
            v -= b
        if v - c < 0:
            return "T"
        else:
            v -= c

=======
Suggestion 3

def solve():
    v,a,b,c = map(int,input().split())
    if v <= a:
        return "F"
    if v <= a+b:
        return "M"
    return "T"
print(solve())

=======
Suggestion 4

def problems243_a():
    v,a,b,c = map(int,input().split())
    #print(v,a,b,c)
    while True:
        if v < a:
            return "F"
        v -= a
        if v < b:
            return "M"
        v -= b
        if v < c:
            return "T"
        v -= c
    return "F"
print(problems243_a())

=======
Suggestion 5

def problems243_a():
    v,a,b,c = map(int,input().split())
    if v <= 0 or v > 100000:
        return
    if a <= 0 or a > 100000:
        return
    if b <= 0 or b > 100000:
        return
    if c <= 0 or c > 100000:
        return
    if v < a:
        return
    if v < b:
        return
    if v < c:
        return

    while v >= 0:
        v -= a
        if v < 0:
            return "F"
        v -= b
        if v < 0:
            return "M"
        v -= c
        if v < 0:
            return "T"

print(problems243_a())

=======
Suggestion 6

def main():
    v, a, b, c = map(int, input().split())
    while True:
        if v - a < 0:
            print('T')
            break
        else:
            v -= a
        if v - b < 0:
            print('F')
            break
        else:
            v -= b
        if v - c < 0:
            print('M')
            break
        else:
            v -= c

=======
Suggestion 7

def main():
    # input
    V, A, B, C = map(int, input().split())

    # compute
    cnt = 0
    while V > 0:
        V -= A
        cnt += 1
        if V <= 0:
            break
        V -= B
        cnt += 1
        if V <= 0:
            break
        V -= C
        cnt += 1
        if V <= 0:
            break

    # output
    if cnt % 3 == 1:
        print('F')
    elif cnt % 3 == 2:
        print('M')
    elif cnt % 3 == 0:
        print('T')

=======
Suggestion 8

def main():
    v, a, b, c = map(int, input().split())
    while v > 0:
        if v - a < 0:
            print("F")
            break
        else:
            v -= a
        if v - b < 0:
            print("M")
            break
        else:
            v -= b
        if v - c < 0:
            print("T")
            break
        else:
            v -= c

=======
Suggestion 9

def main():
    v,a,b,c = map(int,input().split())
    if v < a+b+c:
        if v < a:
            print("F")
        elif v < a+b:
            print("M")
        else:
            print("T")
    else:
        print("T")

=======
Suggestion 10

def main():
    V,A,B,C = map(int,input().split())
    while True:
        if V - A < 0:
            print('T')
            break
        V = V - A
        if V - B < 0:
            print('F')
            break
        V = V - B
        if V - C < 0:
            print('M')
            break
        V = V - C
