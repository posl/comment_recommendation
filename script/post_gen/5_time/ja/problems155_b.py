Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    for a in a_list:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if a%2 == 0 and (a%3 != 0 and a%5 != 0):
            print("DENIED")
            return
    print("APPROVED")

=======
Suggestion 3

def is_evenly_divisible_by_3_or_5(num):
    if num % 2 == 0:
        if num % 3 == 0 or num % 5 == 0:
            return True
        else:
            return False
    else:
        return False

N = int(input())
A = list(map(int, input().split()))

for a in A:
    if is_evenly_divisible_by_3_or_5(a) == False:
        print('DENIED')
        exit()

print('APPROVED')

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                print("DENIED")
                exit()
    print("APPROVED")

=======
Suggestion 5

def check(n):
    if n % 2 == 0:
        if n % 3 == 0 or n % 5 == 0:
            return True
        else:
            return False
    else:
        return True

=======
Suggestion 6

def judge():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 != 0 and A[i] % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")

=======
Suggestion 7

def main():
    num = int(input())
    A = list(map(int, input().split()))
    flag = True
    for i in A:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                flag = False
    if flag:
        print("APPROVED")
    else:
        print("DENIED")

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                print("DENIED")
                exit()
    print("APPROVED")

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 != 0 and A[i] % 5 != 0:
                print("DENIED")
                break
        if i == N-1:
            print("APPROVED")

=======
Suggestion 10

def check():
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                return False
    return True

n = int(input())
a = list(map(int, input().split()))
