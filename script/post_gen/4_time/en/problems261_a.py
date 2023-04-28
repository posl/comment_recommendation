Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L1, R1, L2, R2 = input().split()
    L1 = int(L1)
    R1 = int(R1)
    L2 = int(L2)
    R2 = int(R2)

    if L2 <= R1 and L1 <= R2:
        if L1 <= L2 and R1 <= R2:
            print(R1 - L2)
        elif L2 <= L1 and R2 <= R1:
            print(R2 - L1)
        elif L1 <= L2 and R2 <= R1:
            print(R2 - L2)
        elif L2 <= L1 and R1 <= R2:
            print(R1 - L1)
    else:
        print(0)

=======
Suggestion 2

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l1 <= l2 <= r1 <= r2:
        print(r1 - l2)
    elif l1 <= l2 <= r2 <= r1:
        print(r2 - l2)
    elif l2 <= l1 <= r1 <= r2:
        print(r1 - l1)
    elif l2 <= l1 <= r2 <= r1:
        print(r2 - l1)
    else:
        print(0)

=======
Suggestion 3

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l1 <= l2 <= r1:
        print(r1 - l2)
    elif l2 <= l1 <= r2:
        print(r2 - l1)
    else:
        print(0)

=======
Suggestion 4

def main():
    L1, R1, L2, R2 = map(int, input().split())
    if L1 <= L2 and R1 >= R2:
        print(R2 - L2)
    elif L1 >= L2 and R1 <= R2:
        print(R1 - L1)
    elif L1 <= L2 and R1 <= R2:
        print(R1 - L2)
    elif L1 >= L2 and R1 >= R2:
        print(R2 - L1)
    else:
        print(0)

=======
Suggestion 5

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 <= l2 <= r1 <= r2:
        print(r1-l2)
    elif l2 <= l1 <= r2 <= r1:
        print(r2-l1)
    elif l1 <= l2 <= r2 <= r1:
        print(r2-l2)
    elif l2 <= l1 <= r1 <= r2:
        print(r1-l1)
    else:
        print(0)

=======
Suggestion 6

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l2 <= r1:
        print(max(r1, r2) - l2)
    elif l1 <= r2:
        print(max(r1, r2) - l1)
    else:
        print(0)

=======
Suggestion 7

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 <= l2 <= r1 <= r2 or l2 <= l1 <= r2 <= r1:
        print(r1-l2)
    elif l1 <= l2 <= r2 <= r1 or l2 <= l1 <= r1 <= r2:
        print(r2-l2)
    else:
        print(0)

=======
Suggestion 8

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l1 <= l2 and r1 >= l2:
        print(max(r1, r2) - l2)
    elif l1 <= r2 and r1 >= r2:
        print(r2 - min(l1, l2))
    else:
        print(0)

=======
Suggestion 9

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l2 <= r1 and r2 >= l1:
        print(max(l2, l1) - min(r1, r2))
    else:
        print(0)

=======
Suggestion 10

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l1<=l2 and r1>=l2:
        if r1>=r2:
            print(r2-l2)
        else:
            print(r1-l2)
    elif l1>=l2 and r1<=r2:
        print(r1-l1)
    elif l1>=l2 and l1<=r2:
        if r1>=r2:
            print(r2-l1)
        else:
            print(r1-l1)
    elif l1<=l2 and r1<=r2:
        print(r1-l2)
    else:
        print(0)
