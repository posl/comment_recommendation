Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    V, A, B, C = map(int, input().split())
    if V < A:
        print('F')
    elif V < B:
        print('M')
    elif V < C:
        print('T')
    else:
        print('M')

=======
Suggestion 2

def main():
    V, A, B, C = map(int, input().split())
    if V < A:
        print('F')
    elif V < B:
        print('M')
    elif V < C:
        print('T')
    else:
        if A < B:
            if A < C:
                print('F')
            else:
                print('T')
        else:
            if B < C:
                print('M')
            else:
                print('T')

=======
Suggestion 3

def main():
    v, a, b, c = map(int, input().split())
    if a >= b and a >= c:
        print('F')
    elif b >= c:
        print('M')
    else:
        print('T')

=======
Suggestion 4

def main():
    v, a, b, c = map(int, input().split())
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
Suggestion 5

def main():
    V, A, B, C = map(int, input().split())
    if V == A:
        print("T")
    elif V == B:
        print("M")
    elif V == C:
        print("F")
    elif A > B and A > C:
        print("F")
    elif B > A and B > C:
        print("T")
    else:
        print("M")

=======
Suggestion 6

def main():
    V,A,B,C = map(int,input().split())
    if A > B:
        if B > C:
            print('M')
        else:
            print('T')
    else:
        if A > C:
            print('M')
        else:
            print('F')

=======
Suggestion 7

def main():
    v, a, b, c = map(int, input().split())
    if (v % a) % b == 0 and (v % a) % c == 0:
        print('F')
    elif (v % a) % b == 0:
        print('T')
    elif (v % a) % c == 0:
        print('M')
    else:
        print('F')

main()

=======
Suggestion 8

def main():
    V,A,B,C = map(int, input().split())
    if A >= B and B >= C:
        print('F')
    elif A <= B and B <= C:
        print('M')
    else:
        print('T')

=======
Suggestion 9

def main():
    #input
    v,a,b,c = map(int,input().split())

    #process
    if v - a < 0:
        print("F")
    elif v - a - b < 0:
        print("M")
    elif v - a - b - c < 0:
        print("T")
    else:
        print("M")

=======
Suggestion 10

def main():
    # Read input
    V, A, B, C = map(int, input().split())

    # Solve the problem
    if V < A:
        print("T")
    elif V < A + B:
        print("F")
    elif V < A + B + C:
        print("M")
    else:
        print("T")
