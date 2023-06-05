def main():
    w,h,x,y = map(int, raw_input().split())
    if (w/2.0 == x) and (h/2.0 == y):
        print w*h/2.0, 1
    else:
        print w*h/2.0, 0
