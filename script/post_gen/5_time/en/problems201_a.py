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
    if a[2]-a[1] == a[1]-a[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    A = input().split()
    A = [int(i) for i in A]
    A.sort()
    if A[2]-A[1] == A[1]-A[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    a = input().split()
    a = [int(i) for i in a]
    a.sort()
    if a[2] - a[1] == a[1] - a[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    a = input().rstrip().split()
    a.sort()
    if int(a[2]) - int(a[1]) == int(a[1]) - int(a[0]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    a_1, a_2, a_3 = map(int, input().split())
    if a_3-a_2==a_2-a_1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    # input
    a1, a2, a3 = map(int, input().split())

    # solve
    if a3 - a2 == a2 - a1:
        ans = "Yes"
    else:
        ans = "No"

    # output
    print(ans)

=======
Suggestion 8

def is_arithmetic_sequence(a):
    if a[2]-a[1]==a[1]-a[0]:
        return True
    else:
        return False

a = list(map(int, input().split()))

=======
Suggestion 9

def main():
    input = raw_input()
    input = input.split()
    input = map(int, input)
    input.sort()
    if input[2] - input[1] == input[1] - input[0]:
        print "Yes"
    else:
        print "No"

=======
Suggestion 10

def is_arithmetic_sequence(a):
    if a[0] - a[1] == 0 or a[1] - a[2] == 0:
        return True
    elif a[0] - a[1] == a[1] - a[2]:
        return True
    else:
        return False

a = list(map(int, input().split()))
