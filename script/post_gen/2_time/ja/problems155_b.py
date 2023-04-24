Synthesizing 10/10 solutions (Duplicates hidden)

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
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                print('DENIED')
                exit()
    print('APPROVED')

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    for a in A:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")

=======
Suggestion 4

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    for a in a_list:
        if a % 2 == 0:
            if a % 3 == 0 or a % 5 == 0:
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
                return
    print("APPROVED")
    return

=======
Suggestion 6

def check(num):
    if num % 2 == 0:
        if num % 3 == 0 or num % 5 == 0:
            return True
    else:
        return False

n = int(input())
a = list(map(int, input().split()))

for i in a:
    if check(i) == False:
        print('DENIED')
        exit()

print('APPROVED')

=======
Suggestion 7

def check(n):
    if (n % 2 == 0 and (n % 3 == 0 or n % 5 == 0)):
        return True
    else:
        return False

n = int(input())
a = list(map(int, input().split()))

flag = True
for i in range(n):
    if not check(a[i]):
        flag = False
        break

=======
Suggestion 8

def is_ok(num):
    if num % 2 == 0:
        if num % 3 == 0 or num % 5 == 0:
            return True
    else:
        return False

N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    if is_ok(A[i]) == False:
        print('DENIED')
        exit()
print('APPROVED')

=======
Suggestion 9

def check_if_approved_or_not(num):
    if num % 2 == 0:
        if num % 3 == 0 or num % 5 == 0:
            return True
        else:
            return False
    else:
        return True
