Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    for i in range(0, n//4+1):
        for j in range(0, n//7+1):
            if 4*i + 7*j == n:
                print('Yes')
                return
    print('No')

=======
Suggestion 2

def main():
    n = int(input())
    for i in range(0, n//4+1):
        for j in range(0, n//7+1):
            if 4*i+7*j == n:
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def main():
    n = int(input())
    if n % 4 == 0 or n % 7 == 0:
        print("Yes")
        return
    for i in range(1, n // 4 + 1):
        if (n - 4 * i) % 7 == 0:
            print("Yes")
            return
    print("No")

=======
Suggestion 4

def solve():
    N = int(input())
    for i in range(N//4 + 1):
        if (N - i*4) % 7 == 0:
            print('Yes')
            return
    print('No')

=======
Suggestion 5

def main():
    n = int(input())
    for i in range(0, n//4+1):
        if (n-i*4)%7 == 0:
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def main():
    N = int(input())
    for i in range(0, N+1, 4):
        if (N-i)%7 == 0:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 7

def main():
    N = int(input())
    for i in range(0, 26):
        for j in range(0, 15):
            if (4 * i) + (7 * j) == N:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 8

def main():
    n = int(input())
    ans = False
    for i in range(0, n+1, 4):
        if (n-i)%7 == 0:
            ans = True
            break
    if ans:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    n = int(input())
    if n%4 == 0 or n%7 == 0 or n%11 == 0:
        print('Yes')
        exit()
    for i in range(1, n//4+1):
        for j in range(1, n//7+1):
            if i*4 + j*7 == n:
                print('Yes')
                exit()
    print('No')

=======
Suggestion 10

def judge(n):
    for i in range(0, 26):
        for j in range(0, 15):
            if (i * 4 + j * 7) == n:
                return True
    return False

n = int(input())
