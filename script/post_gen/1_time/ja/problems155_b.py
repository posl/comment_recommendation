Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                print('DENIED')
                return
    print('APPROVED')
    return

=======
Suggestion 2

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
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if a % 2 == 0 and (a % 3 != 0 and a % 5 != 0):
            print("DENIED")
            exit()
    print("APPROVED")

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))

    for i in a:
        if i % 2 == 0:
            if i % 3 == 0 or i % 5 == 0:
                continue
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
        if A[i]%2 == 0:
            if A[i]%3 != 0 and A[i]%5 != 0:
                print("DENIED")
                exit()
    print("APPROVED")

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in A:
        if i % 2 == 0:
            if i % 3 == 0 or i % 5 == 0:
                pass
            else:
                print('DENIED')
                exit()
    print('APPROVED')

=======
Suggestion 7

def check(n):
    if n % 2 == 0:
        if n % 3 == 0 or n % 5 == 0:
            return True
        else:
            return False
    else:
        return True

n = int(input())
a = list(map(int, input().split()))
for i in a:
    if check(i) == False:
        print('DENIED')
        exit()
print('APPROVED')

=======
Suggestion 8

def check(a):
    if a % 2 == 0 and (a % 3 == 0 or a % 5 == 0):
        return True
    else:
        return False

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if check(a[i]) == False:
        print("DENIED")
        exit()
print("APPROVED")

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = "APPROVED"
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                result = "DENIED"
    print(result)

=======
Suggestion 10

def is_approved(ary):
    for i in ary:
        if i % 2 == 0 and (i % 3 != 0 and i % 5 != 0):
            return False
    return True
