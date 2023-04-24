Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                print('DENIED')
                exit()
    print('APPROVED')

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                print('DENIED')
                return
    print('APPROVED')

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 == 0 or A[i] % 5 == 0:
                pass
            else:
                print("DENIED")
                exit()
    print("APPROVED")

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 != 0 and A[i] % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                print("DENIED")
                return

    print("APPROVED")

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                print('DENIED')
                exit()
    print('APPROVED')

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    for i in A:
        if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
            print("DENIED")
            return
    print("APPROVED")

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    for i in range(0, N):
        if A[i] % 2 == 0:
            if A[i] % 3 == 0 or A[i] % 5 == 0:
                continue
            else:
                print('DENIED')
                return
    print('APPROVED')

=======
Suggestion 10

def main():
    # Write your code here
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 == 0 or a[i] % 5 == 0:
                continue
            else:
                print("DENIED")
                return
    print("APPROVED")
