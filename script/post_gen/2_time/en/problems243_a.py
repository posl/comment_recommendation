Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    V, A, B, C = map(int, input().split())
    if A > B:
        A, B = B, A
    if A > C:
        A, C = C, A
    if B > C:
        B, C = C, B

    if A > V:
        print("F")
    elif B > V:
        print("M")
    else:
        print("T")

=======
Suggestion 2

def main():
    V, A, B, C = map(int, input().split())
    if A >= V:
        print('F')
    elif A + B >= V:
        print('M')
    else:
        print('T')

=======
Suggestion 3

def main():
    V, A, B, C = map(int, input().split())
    if V - A <= 0:
        print("F")
    elif V - A - B <= 0:
        print("M")
    elif V - A - B - C <= 0:
        print("T")
    else:
        print("F")

=======
Suggestion 4

def main():
    V, A, B, C = map(int, input().split())
    if V <= A:
        print('F')
    elif V <= A + B:
        print('M')
    else:
        print('T')

=======
Suggestion 5

def main():
    v,a,b,c = map(int,input().split())
    if a <= b and a <= c:
        print('F')
    elif b <= a and b <= c:
        print('M')
    else:
        print('T')

=======
Suggestion 6

def main():
    V, A, B, C = map(int, input().split())
    if V <= A:
        print("T")
    elif V <= A + B:
        print("M")
    elif V <= A + B + C:
        print("F")
    elif A + B + C < V:
        print("M")

main()

=======
Suggestion 7

def main():
    V, A, B, C = map(int, input().split())
    if V % A == 0:
        Takahashi = V // A
    else:
        Takahashi = V // A + 1
    if V % B == 0:
        Takahashi_father = V // B
    else:
        Takahashi_father = V // B + 1
    if V % C == 0:
        Takahashi_mother = V // C
    else:
        Takahashi_mother = V // C + 1
    if Takahashi_father <= Takahashi_mother and Takahashi_father <= Takahashi:
        print("F")
    elif Takahashi_mother <= Takahashi_father and Takahashi_mother <= Takahashi:
        print("M")
    elif Takahashi <= Takahashi_father and Takahashi <= Takahashi_mother:
        print("T")

=======
Suggestion 8

def main():
    v,a,b,c = [int(x) for x in input().split()]
    if v%a == 0:
        print("F")
    elif v%b == 0:
        print("M")
    elif v%c == 0:
        print("T")
    else:
        print("M")

=======
Suggestion 9

def main():
    v, a, b, c = map(int, input().split())
    if a*b*c <= v:
        print("M")
    elif a*b <= v or b*c <= v or c*a <= v:
        print("F")
    else:
        print("T")

=======
Suggestion 10

def main():
    #Read the input
    v,a,b,c = map(int,input().split())
    #The first person to run short of shampoo is Takahashi's father
    if a > v:
        print("F")
    #The first person to run short of shampoo is Takahashi's mother
    elif a + b > v:
        print("M")
    #The first person to run short of shampoo is Takahashi
    else:
        print("T")
