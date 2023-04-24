Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

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
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")
    return

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                print('DENIED')
                return
    print('APPROVED')
    return

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in A:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")
    return

main()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for x in A:
        if x % 2 == 0:
            if x % 3 != 0 and x % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")
    return

main()

=======
Suggestion 7

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
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if a % 2 == 0 and not a % 3 == 0 and not a % 5 == 0:
            print("DENIED")
            return
    print("APPROVED")

=======
Suggestion 9

def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    #compute
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 == 0 or A[i] % 5 == 0:
                pass
            else:
                print('DENIED')
                return
    #output
    print('APPROVED')

=======
Suggestion 10

def isDivisibleBy3Or5(number):
    if number % 3 == 0 or number % 5 == 0:
        return True
    else:
        return False
