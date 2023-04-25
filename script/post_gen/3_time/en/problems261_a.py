Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L1, R1, L2, R2 = map(int, input().split())
    if R1 < L2 or R2 < L1:
        print(0)
    else:
        print(min(R1, R2) - max(L1, L2))

main()

=======
Suggestion 2

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if r1 <= l2 or r2 <= l1:
        print(0)
    else:
        print(min(r1, r2) - max(l1, l2))

=======
Suggestion 3

def solve():
    L1, R1, L2, R2 = map(int, input().split())
    if L1 > L2:
        L1, R1, L2, R2 = L2, R2, L1, R1
    if R1 < L2:
        print(0)
    else:
        print(min(R1, R2) - L2)

=======
Suggestion 4

def main():
    L1, R1, L2, R2 = map(int, input().split())
    if L1 < L2:
        if R1 < L2:
            print(0)
        else:
            print(min(R1, R2) - L2)
    else:
        if R2 < L1:
            print(0)
        else:
            print(min(R1, R2) - L1)

=======
Suggestion 5

def main():
    #input
    L1,R1,L2,R2 = map(int,input().split())

    #output
    if R1 < L2:
        print(0)
    elif R2 < L1:
        print(0)
    else:
        print(min(R1,R2)-max(L1,L2))

=======
Suggestion 6

def paint():
    L1, R1, L2, R2 = map(int, input().split())
    if L1 <= L2 <= R1 or L2 <= L1 <= R2:
        print(min(R1, R2) - max(L1, L2))
    else:
        print(0)

=======
Suggestion 7

def main():
    #input
    l1,r1,l2,r2 = map(int,input().split())
    #compute
    if r1 < l2:
        ans = 0
    elif r2 < l1:
        ans = 0
    else:
        ans = min(r1,r2) - max(l1,l2)
    #output
    print(ans)

=======
Suggestion 8

def main():
    #input
    L1,R1,L2,R2 = map(int,input().split())
    #output
    if L1<=L2 and L2<=R1 and R1<=R2:
        print(R1-L2)
    elif L2<=L1 and L1<=R2 and R2<=R1:
        print(R2-L1)
    elif L2<=L1 and L1<=R1 and R1<=R2:
        print(R1-L1)
    elif L1<=L2 and L2<=R2 and R2<=R1:
        print(R2-L2)
    else:
        print(0)
    return

=======
Suggestion 9

def main():
    # Read input
    L1, R1, L2, R2 = map(int, input().split())

    # Calculate the length of the part of the line painted both red and blue
    result = 0
    if L1 < L2:
        if R1 < L2:
            result = 0
        elif R1 < R2:
            result = R1 - L2
        else:
            result = R2 - L2
    else:
        if R2 < L1:
            result = 0
        elif R2 < R1:
            result = R2 - L1
        else:
            result = R1 - L1

    # Output
    print(result)

=======
Suggestion 10

def main():
    # Read input
    L1, R1, L2, R2 = map(int, input().split())

    # Check if L1 is between L2 and R2
    if L1 >= L2 and L1 <= R2:
        # Check if R1 is between L2 and R2
        if R1 >= L2 and R1 <= R2:
            print(R1 - L1)
        else:
            print(R2 - L1)
    # Check if L2 is between L1 and R1
    elif L2 >= L1 and L2 <= R1:
        # Check if R2 is between L1 and R1
        if R2 >= L1 and R2 <= R1:
            print(R2 - L2)
        else:
            print(R1 - L2)
    else:
        print(0)
