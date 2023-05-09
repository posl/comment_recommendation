Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())

    if A > B:
        print(0)
    elif A == B:
        print(1)
    elif N == 1:
        print(1)
    else:
        print((N-2)*(B-A)+1)

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    print(n//(a+b)*a + min(n%(a+b), a))

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    if a + b == 0:
        print(0)
    elif a == 0:
        print(n)
    else:
        print((n // (a + b)) * a + min(n % (a + b), a))

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    print((N//(A+B))*A + min(A, N%(A+B)))

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    if N == 1:
        if A > 0:
            print(1)
        else:
            print(0)
        return
    if A > B:
        print(0)
        return
    if A == 0 and B > 0:
        print(0)
        return
    if A == 0 and B == 0:
        print(0)
        return
    if A == B:
        print(1)
        return
    if A < B:
        if N == 2:
            print(1)
            return
        if N == 3:
            print(2)
            return
        if N == 4:
            print(2)
            return
        if N == 5:
            print(3)
            return
        if N == 6:
            print(3)
            return
        if N == 7:
            print(4)
            return
        if N == 8:
            print(4)
            return
        if N == 9:
            print(5)
            return
        if N == 10:
            print(5)
            return
        if N == 11:
            print(6)
            return
        if N == 12:
            print(6)
            return
        if N == 13:
            print(7)
            return
        if N == 14:
            print(7)
            return
        if N == 15:
            print(8)
            return
        if N == 16:
            print(8)
            return
        if N == 17:
            print(9)
            return
        if N == 18:
            print(9)
            return
        if N == 19:
            print(10)
            return
        if N == 20:
            print(10)
            return
        if N == 21:
            print(11)
            return
        if N == 22:
            print(11)
            return
        if N == 23:
            print(12)
            return
        if N == 24:
            print(12)
            return
        if N == 25:
            print(13)
            return
        if N == 26:
            print(13)
            return
        if N ==

=======
Suggestion 6

def main():
    N,A,B = map(int,input().split())
    if A+B == 0:
        print(0)
    else:
        print((N//(A+B))*A+min(N%(A+B),A))

=======
Suggestion 7

def main():
    input = input()
    n, a, b = input.split()
    n = int(n)
    a = int(a)
    b = int(b)

    b_count = 0
    r_count = 0

    for i in range(n):
        if (r_count == a + b):
            break
        elif (r_count < a + b):
            if (r_count < a):
                b_count += 1
            else:
                r_count += 1
        else:
            r_count = 0

    print(b_count)

=======
Suggestion 8

def calc_balls(n, a, b):
    if n <= a:
        return n
    else:
        return a + (n - a) % (a + b)

=======
Suggestion 9

def calc_blue_balls(N, A, B):
    #print("N: {}, A: {}, B: {}".format(N, A, B))
    if A == 0:
        return 0
    elif A + B == 1:
        return 1
    elif N <= A:
        return 1
    else:
        return A + (N - A) % (A + B)
