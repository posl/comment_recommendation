def main():
    w,h,x,y = map(int, input().split())
    area = w * h
    half_area = area / 2
    # print(half_area)
    if x == w/2 and y == h/2:
        print(half_area,1)
    else:
        print(half_area,0)
