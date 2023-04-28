Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    A = list(map(int, input().split()))
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    A = [int(x) for x in input().split()]
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    A = input().split()
    A = [int(i) for i in A]
    A.sort()
    if A[1] - A[0] == A[2] - A[1]:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 6

def is_arithmetic_sequence(a1, a2, a3):
    if a1 == a2 and a2 == a3:
        return True
    elif a1 == a2 or a2 == a3 or a1 == a3:
        return False
    elif a1 + a3 == 2 * a2:
        return True
    else:
        return False

a1, a2, a3 = map(int, input().split())

=======
Suggestion 7

def main():
    A = [int(x) for x in input().split()]
    if A[0] == A[1] and A[0] == A[2]:
        print("Yes")
    elif A[0] == A[1] or A[0] == A[2] or A[1] == A[2]:
        print("No")
    else:
        A.sort()
        if A[1] - A[0] == A[2] - A[1]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    A = [int(x) for x in input().split()]
    #print(A)
    A.sort()
    if A[2]-A[1] == A[1]-A[0]:
        print("Yes")
    else:
        print("No")
