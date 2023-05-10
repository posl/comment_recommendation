Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    for i in range(0, n+1, 4):
        if (n - i) % 7 == 0:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    n = int(input())
    for i in range(0, n+1, 4):
        if (n - i) % 7 == 0:
            print('Yes')
            return
    print('No')

=======
Suggestion 3

def solve():
    N = int(input())
    for i in range(N//4+1):
        if (N - 4*i)%7 == 0:
            print("Yes")
            return
    print("No")

=======
Suggestion 4

def check(n):
    for i in range(0, n+1):
        for j in range(0, n+1):
            if 4*i + 7*j == n:
                return True
    return False

n = int(input())
print('Yes' if check(n) else 'No')

=======
Suggestion 5

def solve():
    n = int(input())
    for i in range(0, 25):
        for j in range(0, 15):
            if 4*i + 7*j == n:
                print('Yes')
                return
    print('No')

=======
Suggestion 6

def main():
    n = int(input())
    for i in range(0, n//4 + 1):
        for j in range(0, n//7 + 1):
            if i*4 + j*7 == n:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 7

def main():
    n = int(input())
    if n%4 == 0 or n%7 == 0 or n%11 == 0:
        print("Yes")
    elif n%4 == 3 or n%7 == 3 or n%11 == 3:
        print("No")
    else:
        print("Yes")

=======
Suggestion 8

def main():
    N = int(input())

    for i in range(0, N+1, 4):
        for j in range(0, N+1, 7):
            if i + j == N:
                print("Yes")
                return
    print("No")

=======
Suggestion 9

def main():
    n = int(input())
    for i in range(0, (n//4)+1):
        if (n - (4 * i)) % 7 == 0:
            print('Yes')
            exit()
    print('No')
