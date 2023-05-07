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
