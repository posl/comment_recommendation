Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 != 0 and A[i] % 5 != 0:
                print('DENIED')
                exit()
    print('APPROVED')

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
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
            print("DENIED")
            return
    print("APPROVED")

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i]%2 == 0:
            if a[i]%3 != 0 and a[i]%5 != 0:
                print('DENIED')
                exit()
    print('APPROVED')

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 != 0 and A[i] % 5 != 0:
                print('DENIED')
                return
    print('APPROVED')
    return

=======
Suggestion 6

def check(num):
    if num % 2 == 1:
        return False
    elif num % 3 == 0:
        return True
    elif num % 5 == 0:
        return True
    else:
        return False

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

ans = 'APPROVED'
for i in a:
    if check(i) == False:
        ans = 'DENIED'
        break
print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if a % 2 == 0 and not(a % 3 == 0 or a % 5 == 0):
            print("DENIED")
            return
    print("APPROVED")
    return

=======
Suggestion 9

def is_approved(numbers):
    for number in numbers:
        if number % 2 == 0 and number % 3 != 0 and number % 5 != 0:
            return False
    return True

=======
Suggestion 10

def check():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 == 0 or a[i] % 5 == 0:
                continue
            else:
                return False
    return True
