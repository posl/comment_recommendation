Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    if n % 4 == 0 or n % 7 == 0 or n % 11 == 0 or n % 15 == 0 or n % 19 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    if n % 4 == 0 or n % 7 == 0 or n % 11 == 0:
        print("Yes")
        return
    for i in range(1, n // 4 + 1):
        for j in range(1, n // 7 + 1):
            if 4 * i + 7 * j == n:
                print("Yes")
                return
    print("No")

main()

=======
Suggestion 3

def main():
    n = int(input())
    for i in range(n//4+1):
        for j in range(n//7+1):
            if i*4+j*7 == n:
                print("Yes")
                return
    print("No")
main()

=======
Suggestion 4

def main():
    n = int(input())
    if n % 7 == 0 or n % 4 == 0:
        print("Yes")
        return
    for i in range(1, n // 7 + 1):
        if (n - 7 * i) % 4 == 0:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def main():
    # input
    N = int(input())

    # compute

    # output
    if N%4 == 0 or N%7 == 0 or N%11 == 0:
        print('Yes')
    elif N%4 == 1 and N >= 9:
        print('Yes')
    elif N%4 == 2 and N >= 18:
        print('Yes')
    elif N%4 == 3 and N >= 7:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n = int(input())
    for i in range((n//4)+1):
        for j in range((n//7)+1):
            if (i*4)+(j*7) == n:
                print("Yes")
                return
    print("No")

=======
Suggestion 7

def main():
    N = int(input())
    for i in range(0, 25):
        for j in range(0, 15):
            if 4*i + 7*j == N:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 8

def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print('Yes')
    elif N >= 8 and N % 4 == 3 or N % 7 == 3:
        print('Yes')
    elif N >= 15 and N % 4 == 7 or N % 7 == 7:
        print('Yes')
    elif N >= 22 and N % 4 == 11 or N % 7 == 11:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def solve():
    n = int(input())
    for i in range(0, n//4+1):
        if (n - 4*i)%7 == 0:
            print('Yes')
            return
    print('No')
solve()

=======
Suggestion 10

def main():
    N = int(input())
    #print(N)
    if N%4==0 or N%7==0:
        print("Yes")
    else:
        for i in range(1,15):
            if N-4*i>0 and (N-4*i)%7==0:
                print("Yes")
                return
            elif N-7*i>0 and (N-7*i)%4==0:
                print("Yes")
                return
        print("No")
