Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    V, A, B, C = map(int, input().split())
    if V < A:
        print("F")
    elif V < B:
        print("M")
    elif V < C:
        print("T")
    else:
        print("T")

=======
Suggestion 2

def main():
    V,A,B,C = map(int,input().split())
    if V < A:
        print("F")
    elif V < B:
        print("M")
    elif V < C:
        print("T")

=======
Suggestion 3

def main():
    V,A,B,C = map(int,input().split())
    if V % A == 0:
        print("F")
    elif V % B == 0:
        print("M")
    elif V % C == 0:
        print("T")
    else:
        print("F")

=======
Suggestion 4

def main():
    v, a, b, c = map(int, input().split())
    if v % a == 0 or v % b == 0 or v % c == 0:
        print("F")
    else:
        if v % a <= v % b and v % a <= v % c:
            print("F")
        elif v % b <= v % a and v % b <= v % c:
            print("M")
        else:
            print("T")

=======
Suggestion 5

def main():
    V,A,B,C = map(int,input().split())
    if V <= A:
        print("F")
    elif V <= A+B:
        print("F")
    elif V <= A+B+C:
        print("M")
    else:
        print("T")

=======
Suggestion 6

def main():
    V, A, B, C = map(int, input().split())
    if V >= A+B+C:
        print('T')
    elif V >= A+B:
        print('M')
    elif V >= A:
        print('F')
    else:
        print('T')

=======
Suggestion 7

def main():
    v,a,b,c = map(int,input().split())
    if v % a == 0:
        if v % b == 0:
            if v % c == 0:
                print('T')
            else:
                print('M')
        else:
            print('F')
    else:
        print('F')

=======
Suggestion 8

def main():
    V,A,B,C = map(int,input().split())
    if V >= A and V >= B and V >= C:
        print('T')
    elif V >= A and V >= B and V < C:
        print('M')
    elif V >= A and V < B and V >= C:
        print('M')
    elif V >= A and V < B and V < C:
        print('F')
    elif V < A and V >= B and V >= C:
        print('M')
    elif V < A and V >= B and V < C:
        print('F')
    elif V < A and V < B and V >= C:
        print('F')
    elif V < A and V < B and V < C:
        print('F')
