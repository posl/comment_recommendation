Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print((H-R+1)*(W-C+1))

=======
Suggestion 2

def get_same_edge_num(h,w,r,c):
    return 2*(h-1)*(w-1)-2*(h-1)-2*(w-1)+4

=======
Suggestion 3

def get_number_of_squares(h, w, r, c):
    if h == 1 and w == 1:
        return 0
    elif h == 1:
        return 1
    elif w == 1:
        return 1
    elif r == 1 and c == 1:
        return 0
    elif r == 1:
        return 1
    elif c == 1:
        return 1
    elif r == h and c == w:
        return 0
    elif r == h:
        return 1
    elif c == w:
        return 1
    else:
        return 2

=======
Suggestion 4

def solve(h,w,r,c):
    return 2*(r-1)*(c-1)+(h-r+1)*(c-1)+(w-c+1)*(r-1)+(h-r+1)*(w-c+1)

h,w=map(int,input().split())
r,c=map(int,input().split())
print(solve(h,w,r,c))

=======
Suggestion 5

def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print((h-r+1)*(w-c+1))

=======
Suggestion 6

def get_num(H, W, R, C):
    if R == 1 and C == 1:
        return 0
    elif R == 1 and C == W:
        return 0
    elif R == H and C == 1:
        return 0
    elif R == H and C == W:
        return 0
    elif R == 1 or R == H:
        return 1
    elif C == 1 or C == W:
        return 1
    else:
        return 2

H, W = map(int, input().split())
R, C = map(int, input().split())

print(get_num(H, W, R, C))

=======
Suggestion 7

def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print(H*W-((H-R)*W+(W-C)*R))
