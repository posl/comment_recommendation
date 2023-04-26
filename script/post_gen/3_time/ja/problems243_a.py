Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    V,A,B,C = map(int,input().split())
    if V < A:
        print("F")
    elif V < B:
        print("M")
    elif V < C:
        print("T")
    else:
        print("F")

=======
Suggestion 2

def main():
    V, A, B, C = map(int, input().split())
    if V % A == 0:
        print("F")
    elif V % B == 0:
        print("M")
    elif V % C == 0:
        print("T")
    else:
        print("F")

=======
Suggestion 3

def main():
    v, a, b, c = map(int, input().split())
    if v <= a:
        print("F")
    elif v <= a + b:
        print("M")
    else:
        print("T")

=======
Suggestion 4

def main():
    V, A, B, C = map(int, input().split())

    if V <= A:
        print("T")
    elif V <= A + B:
        print("M")
    else:
        print("F")

=======
Suggestion 5

def main():
    V, A, B, C = map(int, input().split())
    if V % A == 0 and V % B == 0 and V % C == 0:
        print("F")
    elif V % A == 0 and V % B == 0:
        print("T")
    elif V % A == 0 and V % C == 0:
        print("M")
    elif V % B == 0 and V % C == 0:
        print("F")
    elif V % A == 0:
        print("M")
    elif V % B == 0:
        print("T")
    elif V % C == 0:
        print("F")
    else:
        print("M")

=======
Suggestion 6

def main():
    v,a,b,c = map(int,input().split())
    if v%a == 0:
        print('F')
    elif v%b == 0:
        print('M')
    elif v%c == 0:
        print('T')
    else:
        print('F')

=======
Suggestion 7

def main():
    V, A, B, C = map(int, input().split())
    if V % A == 0 or V % B == 0 or V % C == 0:
        print('T')
    else:
        print('F')

=======
Suggestion 8

def main():
    V,A,B,C = map(int,input().split())
    if V <= A:
        print("F")
    elif V <= A+B:
        print("M")
    else:
        print("T")

=======
Suggestion 9

def main():
    v,a,b,c = map(int,input().split())
    if v % a == 0:
        if v % b == 0:
            if v % c == 0:
                print("T")
            else:
                print("M")
        else:
            print("F")
    else:
        print("F")
