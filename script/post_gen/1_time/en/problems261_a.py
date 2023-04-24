Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L1, R1, L2, R2 = map(int, input().split())
    if R1 < L2 or R2 < L1:
        print(0)
    else:
        print(min(R1, R2) - max(L1, L2))

=======
Suggestion 2

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if r1 < l2 or r2 < l1:
        print(0)
    else:
        print(min(r1, r2) - max(l1, l2))

=======
Suggestion 3

def main():
    L1, R1, L2, R2 = map(int, input().split())
    if L2 <= R1 and R1 <= R2:
        print(R1 - L2)
    elif L1 <= R2 and R2 <= R1:
        print(R2 - L1)
    else:
        print(0)

=======
Suggestion 4

def main():
    L1, R1, L2, R2 = map(int, input().split())
    if L2 >= R1 or L1 >= R2:
        print(0)
    elif L1 <= L2 and R1 <= R2:
        print(R1 - L2)
    elif L1 <= L2 and R2 <= R1:
        print(R2 - L2)
    elif L2 <= L1 and R1 <= R2:
        print(R1 - L1)
    elif L2 <= L1 and R2 <= R1:
        print(R2 - L1)

=======
Suggestion 5

def main():
    L1, R1, L2, R2 = map(int, input().split())
    if R2 < L1 or R1 < L2:
        print(0)
        return
    print(min(R1, R2) - max(L1, L2))

=======
Suggestion 6

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 >= r2 or l2 >= r1:
        print(0)
    else:
        print(max(0,min(r1,r2)-max(l1,l2)))

=======
Suggestion 7

def main():
    # read input
    L1, R1, L2, R2 = map(int, input().split())
    # solve problem
    if R1 < L2 or R2 < L1:
        print(0)
    else:
        print(min(R1, R2) - max(L1, L2))

=======
Suggestion 8

def main():
    #input
    L1,R1,L2,R2 = map(int,input().split())

    #calc
    if L1 < L2:
        if R1 < L2:
            ans = 0
        elif R1 < R2:
            ans = R1 - L2
        else:
            ans = R2 - L2
    else:
        if R2 < L1:
            ans = 0
        elif R2 < R1:
            ans = R2 - L1
        else:
            ans = R1 - L1

    #output
    print(ans)

=======
Suggestion 9

def main():
    #read input
    L1, R1, L2, R2 = map(int, input().split())

    #find the length of the part of the line painted both red and blue, as an integer.
    if R1 < L2:
        print(0)
    elif R2 < L1:
        print(0)
    else:
        print(min(R1, R2) - max(L1, L2))

=======
Suggestion 10

def main():
    # Read the input
    L1, R1, L2, R2 = map(int, input().split())

    # Find the length of the part of the line painted both red and blue
    if R1 >= L2 and R1 <= R2:
        length = R1 - L2
    elif R2 >= L1 and R2 <= R1:
        length = R2 - L1
    else:
        length = 0

    # Output the result
    print(length)
