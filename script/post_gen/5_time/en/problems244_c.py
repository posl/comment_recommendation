Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    print(1)
    a = int(input())
    if a == 2:
        print(3)
        a = int(input())
        if a == 4:
            print(5)
            a = int(input())
            if a == 6:
                print(7)
                a = int(input())
                if a == 8:
                    print(9)
                    a = int(input())
                    if a == 10:
                        print(11)
                        a = int(input())
                        if a == 12:
                            print(13)
                            a = int(input())
                            if a == 14:
                                print(15)
                                a = int(input())
                                if a == 16:
                                    print(17)
                                    a = int(input())
                                    if a == 18:
                                        print(19)
                                        a = int(input())
                                        if a == 20:
                                            print(21)
                                            a = int(input())
                                            if a == 22:
                                                print(23)
                                                a = int(input())
                                                if a == 24:
                                                    print(25)
                                                    a = int(input())
                                                    if a == 26:
                                                        print(27)
                                                        a = int(input())
                                                        if a == 28:
                                                            print(29)
                                                            a = int(input())
                                                            if a == 30:
                                                                print(31)
                                                                a = int(input())
                                                                if a == 32:
                                                                    print(33)
                                                                    a = int(input())
                                                                    if a == 34:
                                                                        print(35)
                                                                        a = int(input())
                                                                        if a == 36:
                                                                            print(37)
                                                                            a = int(input())
                                                                            if a == 38:
                                                                                print(39)
                                                                                a = int(input())
                                                                                if a == 40:
                                                                                    print(41)
                                                                                    a = int(input())
                                                                                    if a == 42:
                                                                                        print(43)
                                                                                        a = int(input())
                                                                                        if a == 44:
                                                                                            print(45)
                                                                                            a = int(input())
                                                                                            if a == 46:
                                                                                                print(47)
                                                                                                a = int(input())
                                                                                                if a == 48:
                                                                                                    print(49)
                                                                                                    a = int(input())
                                                                                                    if a == 50:
                                                                                                        print(51)
                                                                                                        a = int(input())
                                                                                                        if a == 52:
                                                                                                            print(53)
                                                                                                            a = int(input())
                                                                                                            if a ==

=======
Suggestion 2

def main():
    N = int(input())
    if N == 1:
        print(1)
        input()
        print(2)
        input()
        print(3)
        input()
        print(4)
        input()
        print(5)
        exit()
    else:
        print(1)
        input()
        print(2*N)
        input()
        print(2)
        input()
        print(2*N-1)
        input()
        print(3)
        input()
        print(2*N-2)
        input()
        print(4)
        input()
        print(2*N-3)
        input()
        print(5)
        input()
        print(2*N-4)
        input()
        print(6)
        input()
        print(2*N-5)
        input()
        print(7)
        input()
        print(2*N-6)
        input()
        print(8)
        input()
        print(2*N-7)
        input()
        print(9)
        input()
        print(2*N-8)
        input()
        print(10)
        input()
        print(2*N-9)
        input()
        print(11)
        input()
        print(2*N-10)
        input()
        print(12)
        input()
        print(2*N-11)
        input()
        print(13)
        input()
        print(2*N-12)
        input()
        print(14)
        input()
        print(2*N-13)
        input()
        print(15)
        input()
        print(2*N-14)
        input()
        print(16)
        input()
        print(2*N-15)
        input()
        print(17)
        input()
        print(2*N-16)
        input()
        print(18)
        input()
        print(2*N-17)
        input()
        print(19)
        input()
        print(2*N-18)
        input()
        print(20)
        input()
        print(2*N-19)
        input()
        print(21)
        input()
        print(2*N-20)
        input()
        print(22)
        input()
        print(2*N-21)
        input()
        print(23)
        input()
        print(2*N-22)
        input()
        print(24)
        input

=======
Suggestion 3

def main():
    n = int(input())
    left = 1
    right = 2*n+1
    while True:
        mid = (left+right)//2
        print(mid)
        flush()
        aoki = int(input())
        if aoki == 0:
            break
        elif aoki == -1:
            right = mid
        elif aoki == 1:
            left = mid
    exit()

=======
Suggestion 4

def main():
    n = int(input())
    aoki = 0
    takahashi = 0
    for i in range(1, 2*n+2):
        print(i)
        aoki = int(input())
        if aoki == 0:
            break
        takahashi = i
    exit()

=======
Suggestion 5

def main():
    n = int(input())
    a = 1
    b = 2 * n + 1
    while True:
        if a == b:
            print(a)
            break
        c = (a + b) // 2
        print(c)
        d = int(input())
        if d == 0:
            break
        elif d == -1:
            b = c
        else:
            a = c + 1

=======
Suggestion 6

def main():
    n = int(input())
    i = 1
    while True:
        print(i)
        i = int(input())
        if i == 0:
            break
        i = i + 1

=======
Suggestion 7

def main():
    n = int(input())
    for i in range(1,2*n+2):
        print(i)
        flush()
        a = int(input())
        if a == 0:
            break

=======
Suggestion 8

def main():
    n = int(input())
    a = 0
    b = 2*n+2
    while True:
        c = (a+b)//2
        print(c)
        s = int(input())
        if s == 0:
            break
        elif (s == 1 and c == a+1) or (s == 2 and c == b-1):
            a = c
        else:
            b = c

=======
Suggestion 9

def main():
    n = int(raw_input().strip())
    print 1
    aoki = int(raw_input().strip())
    if aoki == 0:
        exit(0)
    if aoki == 2 * n + 1:
        print 1
        exit(0)
    print 2 * n + 1
    aoki = int(raw_input().strip())
    if aoki == 0:
        exit(0)
    print 2 * n + 1
    aoki = int(raw_input().strip())
    if aoki == 0:
        exit(0)
    print 2 * n + 1
    aoki = int(raw_input().strip())
    if aoki == 0:
        exit(0)
    print 2 * n + 1
    aoki = int(raw_input().strip())
    if aoki == 0:
        exit(0)
    print 2 * n + 1
    aoki = int(raw_input().strip())
    if aoki == 0:
        exit(0)
    print 2 * n + 1
    aoki = int(raw_input().strip())
    if aoki == 0:
        exit(0)
    print 2 * n + 1
    aoki = int(raw_input().strip())
    if aoki == 0:
        exit(0)
    print 2 * n + 1
    aoki = int(raw_input().strip())
    if aoki == 0:
        exit(0)

=======
Suggestion 10

def main():
    pass
