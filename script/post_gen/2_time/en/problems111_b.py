Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print(N + (111 - N % 111))

=======
Suggestion 2

def main():
    n = int(input())
    if n % 111 == 0:
        print(n)
    else:
        print(n + (111 - n % 111))

=======
Suggestion 3

def main():
    n = int(input())
    if n % 111 == 0:
        print(n)
    else:
        print((n//111+1)*111)

=======
Suggestion 4

def main():
    n = int(input())
    print((n + 111) // 111 * 111)

main()

=======
Suggestion 5

def main():
    n = int(input())
    print((n + 111 - 1) // 111 * 111)

=======
Suggestion 6

def main():
    #input
    N = int(input())
    #compute
    if N%111 == 0:
        print(N)
    else:
        print(111*(N//111+1))
    #output

=======
Suggestion 7

def main():
    N = int(input())
    print((N+111)//111*111)

=======
Suggestion 8

def main():
    #input
    N = int(input())
    #output
    print(N//111*111+111 if N%111!=0 else N)

=======
Suggestion 9

def main():
    N = int(input())
    if N%111 == 0:
        print(N)
    else:
        print(((N//111)+1)*111)
main()

I was wondering if there was a better way to do this, as I feel like my solution is a bit messy. I'm also wondering if there is a way to do this without using any if statements.

I'm just starting out with Python so any help would be greatly appreciated. Thanks!

I'm trying to write a program that will print the first 100 prime numbers. I've got it working, but I'm not sure if there is a more efficient way to do it. Here's what I've got so far:

=======
Suggestion 10

def main():
    N = int(input())
    print(N//111*111+111)
