Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    V, A, B, C = map(int, input().split())
    if V < A:
        print('F')
    elif V < A + B:
        print('M')
    elif V < A + B + C:
        print('T')
    else:
        print('F')

=======
Suggestion 2

def main():
    V, A, B, C = map(int, input().split())
    if V <= A:
        print('T')
    elif V <= A + B:
        print('M')
    else:
        print('F')

=======
Suggestion 3

def main():
    V,A,B,C = map(int,input().split())
    if A > V:
        print("F")
    elif A+B > V:
        print("M")
    elif A+B+C > V:
        print("T")
    else:
        print("F")

=======
Suggestion 4

def main():
    V,A,B,C = map(int,input().split())
    if A > V:
        print("F")
    elif A+B > V:
        print("M")
    else:
        print("T")

=======
Suggestion 5

def main():
    V,A,B,C = map(int,input().split())
    if A >= V:
        print("F")
    elif A+B >= V:
        print("M")
    else:
        print("T")

=======
Suggestion 6

def main():
    v,a,b,c = list(map(int,input().split()))
    if v <= a:
        print("F")
    elif v <= a+b:
        print("M")
    elif v <= a+b+c:
        print("T")
    return

=======
Suggestion 7

def main():
    v,a,b,c = map(int,input().split())
    if v%a == 0:
        if v%b == 0:
            if v%c == 0:
                print("M")
            else:
                print("T")
        else:
            print("F")
    else:
        print("F")

=======
Suggestion 8

def main():
    V,A,B,C = map(int,input().split())
    if V%A == 0:
        if V%B == 0:
            if V%C == 0:
                print("M")
            else:
                print("T")
        else:
            print("F")
    else:
        print("F")

=======
Suggestion 9

def main():
    #入力
    V,A,B,C = map(int,input().split())
    #出力
    if V%A == 0:
        print("F")
    elif V%B == 0:
        print("M")
    elif V%C == 0:
        print("T")

main()

=======
Suggestion 10

def main():
    v,a,b,c = map(int, input().split())
    print("F" if v <= a else "M" if v <= a+b else "T")
