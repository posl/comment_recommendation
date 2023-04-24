Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    W, H, x, y = map(int, input().split())
    if x == W / 2 and y == H / 2:
        print(W * H / 2, 1)
    else:
        print(W * H / 2, 0)

=======
Suggestion 2

def main():
    W,H,x,y = map(int,input().split())
    if x*2==W and y*2==H:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

=======
Suggestion 3

def main():
    W, H, x, y = map(int, input().split())
    if W/2 == x and H/2 == y:
        print(W * H / 2, 1)
    else:
        print(W * H / 2, 0)

=======
Suggestion 4

def main():
    W, H, x, y = map(int, input().split())
    area = W * H / 2
    if W % 2 == 0 and H % 2 == 0 and x == W / 2 and y == H / 2:
        print(area, 1)
    else:
        print(area, 0)

=======
Suggestion 5

def main():
    W,H,x,y = map(int,input().split())
    ans = W*H/2
    if x == W/2 and y == H/2:
        print(ans,1)
    else:
        print(ans,0)

=======
Suggestion 6

def main():
	W, H, x, y = map(int, input().split())

	area = W * H / 2
	if 2 * x == W and 2 * y == H:
		print(area, 1)
	else:
		print(area, 0)

=======
Suggestion 7

def solve(W,H,x,y):
    if W == x and H == y:
        return (W*H)/2, 1
    elif W == x or H == y:
        return (W*H)/2, 0
    else:
        return (W*H)/2, 0

=======
Suggestion 8

def maxArea(W,H,x,y):
    if W/2 == x and H/2 == y:
        return (W*H)/2, 1
    else:
        return max(W*y, H*x), 0

=======
Suggestion 9

def main():
    # Take input
    W,H,x,y = map(int,input().split())
    # Calculate the area of the rectangle
    area = W*H
    # If the point is at the center, then there are two ways to cut the rectangle
    if x == W/2 and y == H/2:
        print(area/2,1)
    # If the point is not at the center, then there is only one way to cut the rectangle
    else:
        print(area/2,0)
