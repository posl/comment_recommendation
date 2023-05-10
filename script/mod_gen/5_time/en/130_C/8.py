def rectangle(w,h,x,y):
    area = w*h
    if (x == w/2) and (y == h/2):
        return [area/2,1]
    else:
        return [area/2,0]

if __name__ == '__main__':
    rectangle()