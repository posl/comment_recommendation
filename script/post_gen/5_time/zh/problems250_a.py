Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print((H-R)*(W-C))

=======
Suggestion 2

def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print((h-r+1)*(w-c+1))

=======
Suggestion 3

def count_square(h,w,r,c):
    count=0
    if r==1 and c==1:
        count=0
    elif r==1 and c==w:
        count=0
    elif r==h and c==1:
        count=0
    elif r==h and c==w:
        count=0
    elif r==1 and c!=1 and c!=w:
        count=1
    elif r==h and c!=1 and c!=w:
        count=1
    elif c==1 and r!=1 and r!=h:
        count=1
    elif c==w and r!=1 and r!=h:
        count=1
    else:
        count=2
    return count

=======
Suggestion 4

def main():
    #input
    H,W=map(int,input().split())
    R,C=map(int,input().split())
    #init
    ans=0
    #calc
    if R==1 or R==H:
        ans+=1
    if C==1 or C==W:
        ans+=1
    #output
    print(ans)

=======
Suggestion 5

def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print((H-R+1)*(W-C+1))

=======
Suggestion 6

def main():
    h = int(input())
    w = int(input())
    r = int(input())
    c = int(input())
    if h == 1 and w == 1:
        print(0)
        return
    if r == 1 and c == 1:
        print(2)
        return
    if r == h and c == w:
        print(2)
        return
    if r == 1 and c == w:
        print(1)
        return
    if r == h and c == 1:
        print(1)
        return
    if r == 1 or r == h or c == 1 or c == w:
        print(3)
        return
    print(4)

=======
Suggestion 7

def problems250_a(H, W, R, C):
    return 2 * (H - R + 1) * (W - C + 1) - (H - R + 1) - (W - C + 1)

=======
Suggestion 8

def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print(H*W - (H*C+W*R-C*R)*2 + 4*R*C - 3*R - 3*C + 4)

=======
Suggestion 9

def get_input():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    return H, W, R, C
