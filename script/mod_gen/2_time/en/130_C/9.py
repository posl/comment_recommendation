def cut_rectangle(w,h,x,y):
    max_area = 0
    max_area = max(max_area, x * h)
    max_area = max(max_area, w * y)
    max_area = max(max_area, (w - x) * h)
    max_area = max(max_area, w * (h - y))
    print(max_area, 1 if w == x or h == y else 0)
cut_rectangle(2,3,1,2)
cut_rectangle(2,2,1,1)
cut_rectangle(1000000000,1000000000,0,0)
cut_rectangle(1000000000,1000000000,1000000000,1000000000)
