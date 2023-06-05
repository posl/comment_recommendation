def count_grid_points_in_or_on_circle(x,y,r):
    import math
    count = 0
    for i in range(math.floor(x-r),math.ceil(x+r)+1):
        for j in range(math.floor(y-r),math.ceil(y+r)+1):
            if math.sqrt((i-x)**2 + (j-y)**2) <= r:
                count += 1
    return count

if __name__ == '__main__':
    count_grid_points_in_or_on_circle()