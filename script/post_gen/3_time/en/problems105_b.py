Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    for i in range(N // 4 + 1):
        for j in range(N // 7 + 1):
            if 4 * i + 7 * j == N:
                print('Yes')
                return
    print('No')

=======
Suggestion 2

def main():
    n = int(input())
    for i in range(n//4+1):
        for j in range(n//7+1):
            if 4*i + 7*j == n:
                print('Yes')
                return
    print('No')

=======
Suggestion 3

def main():
    N = int(input())
    for i in range(N//4+1):
        for j in range(N//7+1):
            if i*4+j*7 == N:
                print('Yes')
                return
    print('No')
    return

=======
Suggestion 4

def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 4 == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N = int(input())
    for i in range(0, N+1):
        for j in range(0, N+1):
            if 4*i + 7*j == N:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 6

def main():
    n = int(input())
    if n < 4:
        print('No')
    elif n == 4:
        print('Yes')
    elif n == 5:
        print('No')
    elif n == 6:
        print('Yes')
    elif n == 7:
        print('No')
    else:
        print('Yes')

=======
Suggestion 7

def main():
    N = int(input())
    for i in range(N//4+1):
        if (N - 4*i) % 7 == 0:
            print("Yes")
            return
    print("No")

main()

I'm not sure if this is the right place to ask this, but I'm not sure where else to go. I'm trying to learn Python, and I'm stuck on a problem that I can't seem to figure out. I'm using Python 3.6.1. I'm trying to make a program that will take a number and print the sum of all the numbers from 1 to that number. For example, if I input 5, it would print 15, because 1+2+3+4+5 = 15. Here is my code:

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num+1):
    sum += i
print(sum)

When I run it, it prints 0. I'm not sure what I'm doing wrong. I've tried using +=, but that doesn't work either. I've also tried using a while loop, but that doesn't work either. Any help would be appreciated.

I'm trying to write a program that will take a number and print the sum of all the numbers from 1 to that number. For example, if I input 5, it would print 15, because 1+2+3+4+5 = 15. Here is my code:

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num+1):
    sum += i
print(sum)

When I run it, it prints 0. I'm not sure what I'm doing wrong. I've tried using +=, but that doesn't work either. I've also tried using a while loop, but that doesn't work either. Any help would be appreciated.

I am having a hard time understanding how to write a program that will take a number and print the sum of all the numbers from 1 to that number. For example, if I input 5, it would print 15, because 1+2+3+4+5 = 15. Here is my code:

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num

=======
Suggestion 8

def main():
    N = int(input())
    if N < 4:
        print('No')
    elif N == 4 or N == 7:
        print('Yes')
    else:
        if N % 4 == 0 or N % 7 == 0 or N % 4 == 7 or N % 7 == 4:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    N = int(input())
    if N < 4 or N == 5 or N == 6:
        print("No")
    else:
        print("Yes")
