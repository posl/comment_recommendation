def maxArea(W,H,x,y):
    if W/2 == x and H/2 == y:
        return (W*H)/2, 1
    else:
        return max(W*y, H*x), 0
