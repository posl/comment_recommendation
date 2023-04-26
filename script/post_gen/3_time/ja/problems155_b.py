Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")
    return

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
    return

=======
Suggestion 3

def check(num):
    if num % 2 == 0:
        if num % 3 == 0 or num % 5 == 0:
            return True
        else:
            return False
    else:
        return True

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))

    for a in A:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                print("DENIED")
                exit()
    print("APPROVED")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0 and (i % 3 != 0 and i % 5 != 0):
            print("DENIED")
            break
    else:
        print("APPROVED")

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 != 0 and A[i] % 5 != 0:
                print("DENIED")
                exit()
    print("APPROVED")

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i]%2 == 0:
            if a[i]%3 != 0 and a[i]%5 != 0:
                print("DENIED")
                return
    print("APPROVED")
    return

=======
Suggestion 8

def check():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                return False
    return True

=======
Suggestion 9

def check(n):
    if n % 2 == 0:
        if n % 3 == 0 or n % 5 == 0:
            return True
    return False

n = int(input())
a = list(map(int, input().split()))
for i in a:
    if not check(i):
        print("DENIED")
        exit()
print("APPROVED")

=======
Suggestion 10

def check():
    n = int(input())
    a_list = list(map(int, input().split()))
    for a in a_list:
        if a % 2 == 0 and (a % 3 != 0 and a % 5 != 0):
            return False
    return True

print("APPROVED" if check() else "DENIED")
