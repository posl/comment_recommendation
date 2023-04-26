Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[1] - a[0] == a[2] - a[1]:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 3

def main():
    A = list(map(int,input().split()))
    A.sort()
    if A[2]-A[1] == A[1]-A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[2]-a[1] == a[1]-a[0]:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 5

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[1] - a[0] == a[2] - a[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[2]-a[1] == a[1]-a[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def solve():
    a = list(map(int, input().split()))
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    A = input().split()
    A = list(map(int, A))
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    A = list(map(int, input().split()))

    A.sort()

    if A[1] - A[0] == A[2] - A[1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    #入力
    a,b,c = map(int,input().split())
    #出力
    if (a==b==c) or (a==b and b!=c) or (a==c and c!=b) or (b==c and c!=a):
        print("Yes")
    else:
        print("No")
