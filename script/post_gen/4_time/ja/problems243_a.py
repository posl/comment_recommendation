Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    v, a, b, c = map(int, input().split())
    while v > 0:
        v -= a
        if v <= 0:
            print('T')
            return
        v -= b
        if v <= 0:
            print('M')
            return
        v -= c
        if v <= 0:
            print('F')
            return

=======
Suggestion 2

def main():
    v,a,b,c = map(int,input().split())
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
    v,a,b,c = map(int,input().split())
    while v >= 0:
        v -= a
        if v < 0:
            print("F")
            return
        v -= b
        if v < 0:
            print("M")
            return
        v -= c
        if v < 0:
            print("T")
            return

=======
Suggestion 4

def main():
    v,a,b,c = map(int,input().split())
    if v <= a:
        print("F")
    elif v <= a+b:
        print("M")
    elif v <= a+b+c:
        print("T")

=======
Suggestion 5

def problem243_a():
    v,a,b,c = map(int,input().split())
    while v > 0:
        v -= a
        if v <= 0:
            print("T")
            return
        v -= b
        if v <= 0:
            print("M")
            return
        v -= c
        if v <= 0:
            print("F")
            return

=======
Suggestion 6

def main():
    v,a,b,c = map(int,input().split())
    while True:
        if v <= 0:
            print("F")
            break
        else:
            v -= a
            if v <= 0:
                print("T")
                break
            else:
                v -= b
                if v <= 0:
                    print("M")
                    break
                else:
                    v -= c
                    if v <= 0:
                        print("F")
                        break
                    else:
                        continue

=======
Suggestion 7

def solve():
    v,a,b,c = map(int,input().split())
    if v % a == 0:
        print("T")
    elif v % b == 0:
        print("T")
    elif v % c == 0:
        print("T")
    else:
        print("F")

=======
Suggestion 8

def problems243_a():
    V,A,B,C = map(int,input().split())
    if V % A == 0:
        print('T')
    elif V % B == 0:
        print('T')
    elif V % C == 0:
        print('T')
    elif V % A + V % B == 0:
        print('T')
    elif V % A + V % C == 0:
        print('T')
    elif V % B + V % C == 0:
        print('T')
    elif V % A + V % B + V % C == 0:
        print('T')
    else:
        print('F')

=======
Suggestion 9

def shampoo(V, A, B, C):
    if V < A:
        return 'F'
    elif V < A + B:
        return 'M'
    elif V < A + B + C:
        return 'T'
