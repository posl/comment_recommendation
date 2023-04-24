Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    v, a, b, c = map(int, input().split())
    if v <= a:
        print('F')
    elif v <= a + b:
        print('M')
    else:
        print('T')

main()

=======
Suggestion 2

def main():
    v,a,b,c = map(int, input().split())
    if a <= b and a <= c:
        print("F")
    elif b <= a and b <= c:
        print("M")
    elif c <= a and c <= b:
        print("T")

=======
Suggestion 3

def main():
    v,a,b,c = map(int,input().split())
    x = v//a
    y = v//b
    z = v//c
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i*a + j*b + k*c == v:
                    print("F" if i < j < k else "M" if i < k < j else "T")
                    return

=======
Suggestion 4

def main():
    V, A, B, C = [int(x) for x in input().split()]
    if V < A:
        print("F")
    elif V < B:
        print("M")
    elif V < C:
        print("T")
    else:
        print("M")

=======
Suggestion 5

def main():
    V, A, B, C = map(int, input().split())
    if A > B:
        if B > C:
            print('F')
        elif A > C:
            print('M')
        else:
            print('T')
    else:
        if A > C:
            print('M')
        elif B > C:
            print('T')
        else:
            print('F')

=======
Suggestion 6

def main():
    V, A, B, C = map(int, input().split())
    if A >= B:
        if B >= C:
            print("F")
        elif A >= C:
            print("M")
        else:
            print("T")
    else:
        if A >= C:
            print("M")
        elif B >= C:
            print("T")
        else:
            print("F")

=======
Suggestion 7

def main():
    v,a,b,c = map(int, input().split())
    if a > b:
        if a > c:
            print('F')
        else:
            print('T')
    else:
        if b > c:
            print('M')
        else:
            print('T')

main()

Problem B

=======
Suggestion 8

def main():
    V, A, B, C = map(int, input().split())
    if A > B:
        if B > C:
            print("T")
        else:
            if A > C:
                print("T")
            else:
                print("F")
    else:
        if A > C:
            print("T")
        else:
            if B > C:
                print("T")
            else:
                print("M")

=======
Suggestion 9

def main():
    v,a,b,c = map(int, input().split())
    if a > b:
        if b > c:
            print('F')
        else:
            print('M')
    else:
        if a > c:
            print('F')
        else:
            print('T')

=======
Suggestion 10

def main():
    v,a,b,c = map(int,input().split())
    if (v-a)%min(b,c) == 0:
        print("F")
    else:
        print("M")
