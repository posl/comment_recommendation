Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print( (H-R+1)*(W-C+1) )

=======
Suggestion 2

def problems250_a():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print((H-R+1)*(W-C+1))
    return

problems250_a()

=======
Suggestion 3

def get_count(h,w,r,c):
    count = 0
    if r == 1:
        if c == 1:
            count = 0
        elif c == w:
            count = 0
        else:
            count = 1
    elif r == h:
        if c == 1:
            count = 0
        elif c == w:
            count = 0
        else:
            count = 1
    else:
        if c == 1:
            count = 1
        elif c == w:
            count = 1
        else:
            count = 2
    return count

=======
Suggestion 4

def getcount(h,w,r,c):
    count = 0
    if r == 1:
        if c == 1:
            count = 2
        elif c == w:
            count = 2
        else:
            count = 3
    elif r == h:
        if c == 1:
            count = 2
        elif c == w:
            count = 2
        else:
            count = 3
    else:
        if c == 1:
            count = 3
        elif c == w:
            count = 3
        else:
            count = 4
    return count

=======
Suggestion 5

def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    ans = 0
    for i in range(1,h+1):
        for j in range(1,w+1):
            if abs(i-r)+abs(j-c)==1:
                ans+=1
    print(ans)

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    if r == 1 and c == 1:
        print(0)
        return

    if r == 1 and c == w:
        print(0)
        return

    if r == h and c == 1:
        print(0)
        return

    if r == h and c == w:
        print(0)
        return

    if r == 1 or r == h:
        print(1)
        return

    if c == 1 or c == w:
        print(1)
        return

    print(2)

=======
Suggestion 7

def get_num_of_same_edge_squares(h,w,r,c):
    num = 0
    if r == 1 and c == 1:
        num = 0
    elif r == 1 and c == w:
        num = 0
    elif r == h and c == 1:
        num = 0
    elif r == h and c == w:
        num = 0
    elif r == 1:
        num = 1
    elif r == h:
        num = 1
    elif c == 1:
        num = 1
    elif c == w:
        num = 1
    else:
        num = 2
    return num
