Synthesizing 10/10 solutions (Duplicates hidden)

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
    L1, R1, L2, R2 = map(int, input().split())
    if R1 <= L2 or R2 <= L1:
        print(0)
    elif L1 <= L2 and R1 <= R2:
        print(R1 - L2)
    elif L1 <= L2 and R1 >= R2:
        print(R2 - L2)
    elif L1 >= L2 and R1 <= R2:
        print(R1 - L1)
    elif L1 >= L2 and R1 >= R2:
        print(R2 - L1)

=======
Suggestion 3

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l2 <= l1 and l1 <= r2:
        if r1 <= r2:
            print(r1-l1)
        else:
            print(r2-l1)
    elif l1 <= l2 and l2 <= r1:
        if r1 <= r2:
            print(r1-l2)
        else:
            print(r2-l2)
    else:
        print(0)

=======
Suggestion 4

def main():
    L1, R1, L2, R2 = map(int, input().split())
    if L1 == L2:
        print(R1 - L2)
    elif L1 > L2:
        if R1 < R2:
            print(R1 - L2)
        else:
            print(R2 - L2)
    else:
        if R1 < R2:
            print(R1 - L1)
        else:
            print(R2 - L1)

=======
Suggestion 5

def main():
    #input
    L1,R1,L2,R2 = map(int,input().split())
    #compute
    if L1 <= L2 <= R1:
        if R2 <= R1:
            ans = R2-L2
        else:
            ans = R1-L2
    elif L2 <= L1 <= R2:
        if R1 <= R2:
            ans = R1-L1
        else:
            ans = R2-L1
    else:
        ans = 0
    #output
    print(ans)

=======
Suggestion 6

def main():
    # read input
    L1, R1, L2, R2 = map(int, input().split())

    # calc
    if R1 < L2:
        result = 0
    elif R2 < L1:
        result = 0
    else:
        result = min(R1, R2) - max(L1, L2)

    # print
    print(result)

=======
Suggestion 7

def main():
    #Read the input
    L1, R1, L2, R2 = map(int, input().split())
    #Check if the intervals overlap
    if L2 >= R1 or L1 >= R2:
        print(0)
    else:
        print(min(R1, R2) - max(L1, L2))

=======
Suggestion 8

def main():
    #get input
    l1,r1,l2,r2 = map(int,input().split())
    #find the length of the part of the line painted both red and blue
    if l2 <= r1 and l1 <= r2:
        answer = min(r1,r2) - max(l1,l2)
    else:
        answer = 0
    #output
    print(answer)

=======
Suggestion 9

def main():
    # get input
    l1,r1,l2,r2 = map(int,input().split())

    # check if the parts are adjacent
    if r1 < l2:
        print(0)
    elif r2 < l1:
        print(0)
    elif r1 == l2:
        print(0)
    elif r2 == l1:
        print(0)
    else:
        # get the part painted both red and blue
        if l1 < l2:
            l = l2
        else:
            l = l1
        if r1 < r2:
            r = r1
        else:
            r = r2
        print(r-l)
