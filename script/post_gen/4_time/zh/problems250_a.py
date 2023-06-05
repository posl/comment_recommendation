Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print((h-r+1)*(w-c+1))

=======
Suggestion 2

def solve(h, w, r, c):
    return 2*(h-r+1)*(w-c+1)-h*w

=======
Suggestion 3

def getNumOfSquares(h, w, r, c):
    numOfSquares = 0
    if r > 1:
        numOfSquares += 1
    if r < h:
        numOfSquares += 1
    if c > 1:
        numOfSquares += 1
    if c < w:
        numOfSquares += 1
    return numOfSquares

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    print((H - R + 1) * (W - C + 1))

=======
Suggestion 5

def get_input():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    return h,w,r,c

=======
Suggestion 6

def problem250_a():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print((h-r+1)*(w-c+1))

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print(2*(h-1)*(w-1) - (h-1) - (w-1) + 1)
main()

=======
Suggestion 8

def problem250a():
    h,w = map(int,input().split())
    r,c = map(int,input().split())
    print((h-r+1)*(w-c+1))
