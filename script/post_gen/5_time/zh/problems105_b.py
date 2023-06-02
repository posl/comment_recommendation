Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    for i in range(0, n//4 + 1):
        for j in range(0, n//7 + 1):
            if i * 4 + j * 7 == n:
                print("Yes")
                return
    print("No")

=======
Suggestion 2

def main():
    N = int(input())
    for i in range(0, N):
        for j in range(0, N):
            if (4*i+7*j) == N:
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0:
        print('Yes')
        return
    for i in range(1, N // 4 + 1):
        if (N - 4 * i) % 7 == 0:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def main():
    n = int(input())
    print("Yes" if n % 7 == 0 or n % 4 == 0 or n % 11 == 0 or n % 15 == 0 or n % 19 == 0 or n % 20 == 0 or n % 24 == 0 or n % 28 == 0 or n % 31 == 0 or n % 35 == 0 or n % 39 == 0 or n % 43 == 0 or n % 44 == 0 or n % 47 == 0 or n % 48 == 0 or n % 51 == 0 or n % 55 == 0 or n % 59 == 0 or n % 60 == 0 or n % 64 == 0 or n % 67 == 0 or n % 68 == 0 or n % 71 == 0 or n % 72 == 0 or n % 75 == 0 or n % 76 == 0 or n % 79 == 0 or n % 80 == 0 or n % 84 == 0 or n % 88 == 0 or n % 91 == 0 or n % 92 == 0 or n % 95 == 0 or n % 96 == 0 or n % 99 == 0 or n % 100 == 0 else "No")

=======
Suggestion 5

def main():
    n = int(input())
    for i in range(0, n//4+1):
        for j in range(0, n//7+1):
            if 4*i+7*j == n:
                print('Yes')
                return
    print('No')

=======
Suggestion 6

def main():
    n = int(input())
    if n % 7 == 0 or n % 4 == 0:
        print("Yes")
        return
    for i in range(1, 15):
        if n - 7 * i < 0:
            print("No")
            return
        if (n - 7 * i) % 4 == 0:
            print("Yes")
            return
    print("No")

=======
Suggestion 7

def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print("Yes")
    elif N % 4 == 3:
        print("Yes")
    elif N % 7 == 6:
        print("Yes")
    elif N % 11 == 9:
        print("Yes")
    elif N % 4 == 2:
        print("Yes")
    elif N % 7 == 5:
        print("Yes")
    elif N % 11 == 7:
        print("Yes")
    elif N % 4 == 1:
        print("Yes")
    elif N % 7 == 4:
        print("Yes")
    elif N % 11 == 2:
        print("Yes")
    elif N % 4 == 0:
        print("Yes")
    elif N % 7 == 0:
        print("Yes")
    elif N % 11 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    N = int(input())
    for i in range(0, N//4+1):
        for j in range(0, N//7+1):
            if i*4 + j*7 == N:
                print('Yes')
                return
    print('No')

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    while True:
        try:
            N = int(input('请输入一个1到100之间的整数：'))
            if 1 <= N <= 100:
                break
            else:
                print('输入的数不在范围内，请重新输入')
        except:
            print('输入的数不是整数，请重新输入')
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print('Yes')
    elif N % 4 == 3 or N % 7 == 3 or N % 11 == 3:
        print('No')
    else:
        print('Yes')
