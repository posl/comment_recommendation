Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = (i + 1) % 2
    if sum(a) == 0:
        print(0)
    else:
        print(1)
        print(b.index(1) + 1)
main()

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*n
    for i in range(n):
        b[i] = (a[i] + sum(b[i::i+1])) % 2
    print(sum(b))
    print(*[i+1 for i in range(n) if b[i]])

=======
Suggestion 3

def get_good_choice(N, a):
    if N == 1:
        if a[0] == 1:
            return [1]
        else:
            return []
    if N == 2:
        if a[0] == a[1]:
            if a[0] == 0:
                return []
            else:
                return [1]
        else:
            return []
    if N == 3:
        if a[0] == a[1] and a[1] == a[2]:
            if a[0] == 0:
                return []
            else:
                return [1]
        else:
            return []
    if N % 2 == 0:
        if a[0] == a[N - 1]:
            if a[0] == 0:
                return []
            else:
                return [1]
        else:
            return []
    else:
        if a[0] == a[N - 1]:
            if a[0] == 0:
                return []
            else:
                return [1]
        else:
            return []

N = int(input())
a = list(map(int, input().split()))
choice = get_good_choice(N, a)

=======
Suggestion 4

def check(a):
    for i in range(1, len(a) + 1):
        if a[i - 1] != 0 and a[i - 1] != 1:
            return False
    return True

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    b = []
    for i in range(n):
        if a[i] == 1:
            s += 1
            b.append(i + 1)
    if s == 0:
        print(0)
    else:
        print(s)
        print(*b)

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    i = N
    while i > 0:
        if a[i - 1] == 1:
            b[i - 1] = 1
            j = 2
            while i * j <= N:
                a[i * j - 1] = 1 - a[i * j - 1]
                j += 1
        i -= 1
    print(sum(b))
    for i in range(N):
        if b[i] == 1:
            print(i + 1, end=' ')
    print()

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    if N == 1:
        if A[0] == 1:
            print(1)
            print(1)
        else:
            print(0)
    elif N == 2:
        if A[0] == 0 and A[1] == 1:
            print(1)
            print(2)
        elif A[0] == 1 and A[1] == 0:
            print(1)
            print(1)
        elif A[0] == 1 and A[1] == 1:
            print(2)
            print(1, 2)
        else:
            print(0)
    else:
        #print('N = ', N)
        #print('A = ', A)
        #print('A[0] = ', A[0])
        #print('A[1] = ', A[1])
        #print('A[2] = ', A[2])
        #print('A[3] = ', A[3])
        if A[0] == 1:
            if A[1] == 0 and A[2] == 0 and A[3] == 0:
                print(1)
                print(1)
            elif A[1] == 1 and A[2] == 0 and A[3] == 0:
                print(2)
                print(1, 2)
            elif A[1] == 0 and A[2] == 1 and A[3] == 0:
                print(2)
                print(1, 3)
            elif A[1] == 0 and A[2] == 0 and A[3] == 1:
                print(2)
                print(1, 4)
            elif A[1] == 1 and A[2] == 1 and A[3] == 0:
                print(3)
                print(1, 2, 3)
            elif A[1] == 1 and A[2] == 0 and A[3] == 1:
                print(3)
                print(1, 2, 4)
            elif A[1] == 0 and A[2

=======
Suggestion 8

def solve(n, a):
    if sum(a) == 0:
        return [0]
    if n >= 3 and a[0] == 0 and a[1] == 0 and a[2] == 0:
        return [-1]
    if n >= 2 and a[0] == 0 and a[1] == 0:
        return [-1]
    if n >= 2 and a[0] == 1 and a[1] == 0:
        return [-1]
    if n >= 2 and a[0] == 1 and a[1] == 1:
        return [-1]
    if n >= 2 and a[0] == 0 and a[1] == 1:
        return [-1]
    if n >= 3 and a[0] == 1 and a[1] == 0 and a[2] == 1:
        return [-1]
    if n >= 3 and a[0] == 1 and a[1] == 1 and a[2] == 1:
        return [-1]
    if n >= 3 and a[0] == 0 and a[1] == 1 and a[2] == 1:
        return [-1]
    if n >= 4 and a[0] == 1 and a[1] == 0 and a[2] == 0 and a[3] == 1:
        return [-1]
    if n >= 4 and a[0] == 1 and a[1] == 1 and a[2] == 0 and a[3] == 1:
        return [-1]
    if n >= 4 and a[0] == 0 and a[1] == 1 and a[2] == 0 and a[3] == 1:
        return [-1]
    if n >= 4 and a[0] == 0 and a[1] == 1 and a[2] == 0 and a[3] == 0:
        return [-1]
    if n >= 4 and a[0] == 1 and a[1] == 1 and a[2] == 0 and a[3] == 0:
        return [-1]
    if n >=

=======
Suggestion 9

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N, 0, -1):
        s = 0
        for j in range(i, N + 1, i):
            s += b[j - 1]
        if s % 2 != a[i - 1]:
            b[i - 1] = 1
    M = sum(b)
    print(M)
    if M > 0:
        print(*[i + 1 for i in range(N) if b[i] == 1])

=======
Suggestion 10

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N):
        if a[i] == 1:
            b[i] = 1
    if sum(b) == 0:
        print(0)
        return
    print(sum(b))
    for i in range(N):
        if b[i] == 1:
            print(i + 1, end=" ")
    print()
