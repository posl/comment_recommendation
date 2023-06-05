Synthesizing 10/10 solutions

=======
Suggestion 1

def is_even_num(num):
    if num % 2 == 0:
        return True
    else:
        return False

=======
Suggestion 2

def is_divisible_by_3_or_5(n):
    return n % 3 == 0 or n % 5 == 0

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                print('DENIED')
                exit()
    print('APPROVED')

=======
Suggestion 4

def check(x):
    if x % 2 == 0 and (x % 3 == 0 or x % 5 == 0):
        return True
    return False

n = int(input())
a = list(map(int, input().split()))

for x in a:
    if check(x) == False:
        print("DENIED")
        exit()

print("APPROVED")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i]%2 == 0:
            if a[i]%3 != 0 and a[i]%5 != 0:
                print("DENIED")
                exit()
    print("APPROVED")

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    for a in A:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")
    return

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0 and (a[i] % 3 != 0 and a[i] % 5 != 0):
            print('DENIED')
            return
    print('APPROVED')

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0:
            if not (i % 3 == 0 or i % 5 == 0):
                print("DENIED")
                exit()
    print("APPROVED")

=======
Suggestion 9

def main():
    N = int(input())
    A = input().split()
    flag = True
    for i in range(N):
        if int(A[i])%2 == 0:
            if (int(A[i])%3 != 0) and (int(A[i])%5 != 0):
                flag = False
                break
    if flag:
        print('APPROVED')
    else:
        print('DENIED')

=======
Suggestion 10

def checkio(data):
    #replace this for solution
    return 0
