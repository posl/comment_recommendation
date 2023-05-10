Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h,m = map(int,input().split())
    if m == 0:
        if h == 23:
            h = 0
        else:
            h += 1
    else:
        m = 60 - m
        if h == 23:
            h = 0
        else:
            h += 1
    print(h,m)

=======
Suggestion 2

def main():
    H, M = map(int, input().split())
    if M < 30:
        H = H - 1
        if H < 0:
            H = 23
        M = M + 30
    else:
        M = M - 30
    print("{0:02d} {1:02d}".format(H, M))
main()

=======
Suggestion 3

def main():
    h, m = map(int, input().split())
    while True:
        if m == 59:
            h += 1
            m = 0
        else:
            m += 1
        if h == 24:
            h = 0
        if str(h)[::-1] == str(m):
            print("{0:02d} {1:02d}".format(h, m))
            break

=======
Suggestion 4

def main():
    H, M = map(int, input().split())
    if M < 30:
        if H == 0:
            print(23, M+30)
        else:
            print(H-1, M+30)
    else:
        print(H, M-30)

=======
Suggestion 5

def main():
    h, m = map(int, input().split())
    while True:
        m += 1
        if m == 60:
            m = 0
            h += 1
        if h == 24:
            h = 0
        if str(h).zfill(2)[::-1] == str(m).zfill(2):
            print(str(h).zfill(2), str(m).zfill(2))
            break

=======
Suggestion 6

def main():
    h, m = map(int, input().split())
    if m == 0:
        print(h, 0)
        return
    if m <= 12:
        print(h, m)
        return
    if h == 23:
        print(0, m - 12)
        return
    print(h + 1, m - 12)

=======
Suggestion 7

def main():
    H, M = map(int, input().split())
    if M < 30:
        H -= 1
        M += 30
    else:
        M -= 30
    print("{0:02d} {1:02d}".format(H, M))

=======
Suggestion 8

def main():
    H,M = map(int,input().split())
    M = M + 60
    if M > 59:
        H = H + 1
        M = M - 60
    if H > 23:
        H = H - 24
    print(str(H).zfill(2), str(M).zfill(2))

=======
Suggestion 9

def main():
    h,m = map(int,input().split())
    if m == 0:
        h += 1
        m = 0
    elif m <= 3:
        m = 0
    elif m <= 13:
        m = 10
    elif m <= 23:
        m = 20
    elif m <= 33:
        m = 30
    elif m <= 43:
        m = 40
    elif m <= 53:
        m = 50
    else:
        h += 1
        m = 0
    if h == 24:
        h = 0
    print(str(h).zfill(2) + " " + str(m).zfill(2))
