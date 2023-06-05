def main():
    a,b,x = map(int,input().split())
    #水的体积
    v = x/a
    #瓶子的倾斜角度
    import math
    if v < a*b/2:
        #瓶子的倾斜角度
        theta = math.atan2(a*b-2*v,a**2)/(2*math.pi)*360
    else:
        #瓶子的倾斜角度
        theta = math.atan2(2*(a*b-v),b**2)/(2*math.pi)*360
    print(theta)
    return
